
from app_list.bigcommerce import BigCommerceActions
from app_list.shopify_app import ShopifyActions
from enums import AppName

APP_TO_ACTIONS_MAP = {
    AppName.SHOPIFY: ShopifyActions,
    AppName.BIGCOMMERCE: BigCommerceActions
}
