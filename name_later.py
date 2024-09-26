from typing import Any, Dict

from app_list.config import APP_TO_ACTIONS_MAP
from app_list.models import App, OrganizationApp
from enums import AppName


def execute_action(function_name: str, organization_id: int, app_id: int, **kwargs) -> Dict[str, Any]:
    try:
        app = OrganizationApp.objects.get(app_id=app_id, organization_id=organization_id)

        # Get the access token and API URL from the app
        #access_token = app.app_specific_params['auth_token']
        #api_url = app.get_api_url(app.app_specific_params['store_name'])

        # Get the appropriate action class based on the app name
        app_name = AppName(app.app.name)
        action_class = APP_TO_ACTIONS_MAP.get(app_name)

        if not action_class:
            raise ValueError(f"No action class found for app: {app_name}")

        # Get the method from the action class
        method = getattr(action_class, function_name, None)

        if not method:
            raise ValueError(f"Function {function_name} not found in {action_class.__name__}")

        # Execute the method with the access token, API URL, and any additional arguments
        result = method(app.app_specific_params, **kwargs)
        return {"success": True, "data": result}

    except App.DoesNotExist:
        return {"success": False, "error": f"App with id {app_id} not found for the given organization"}



