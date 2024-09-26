from bigcommerce import api

from templates.ecommerce import EcommerceActionList


class BigCommerceActions(EcommerceActionList):
    @classmethod
    def _initialize_session(cls, extra_params: dict):
        return api.BigcommerceApi(
            client_id=extra_params['client_id'],
            store_hash=extra_params['store_hash'],
            access_token=extra_params['access_token']
        )

    @classmethod
    def get_customer_by_email(cls, extra_params: dict, email: str) -> dict:
        client = cls._initialize_session(extra_params)
        customers = client.Customers.all(email=email)
        return customers[0].to_dict() if customers else {}

    @classmethod
    def get_customer_by_phone(cls, extra_params: dict, phone: str) -> dict:
        # client = cls._initialize_session(extra_params)
        # customers = client.Customers.all(phone=phone)
        # return customers[0].to_dict() if customers else {}
        return {'customer_id': '1', 'email': 'test@test.com', 'phone': '9876543210'}

    @classmethod
    def get_most_recent_customer_orders(cls, extra_params: dict, customer_id: str, limit: int = 10) -> dict:
        client = cls._initialize_session(extra_params)
        orders = client.Orders.all(customer_id=customer_id, limit=limit, sort='date_created:desc')
        return [order.to_dict() for order in orders]

    @classmethod
    def cancel_order(cls, extra_params: dict, order_id: str) -> dict:
        # client = cls._initialize_session(extra_params)
        # order = client.Orders.get(order_id)
        # cancelled_order = order.update(status_id=5)  # Assuming 5 is the status ID for cancelled orders
        # return {"success": True, "message": "Successfully cancelled order"}
        return {"success": True, "message": "Successfully cancelled order"}

    @classmethod
    def create_refund(cls, extra_params: dict, order_id: str) -> dict:
        client = cls._initialize_session(extra_params)
        order = client.Orders.get(order_id)
        refund = client.OrderRefunds.create(order)
        return refund.to_dict() if refund else {}

    @classmethod
    def get_order_by_order_number(cls, extra_params: dict, order_id: str) -> dict:
        client = cls._initialize_session(extra_params)
        order = client.Orders.get(order_id)
        return order.to_dict()

    @classmethod
    def get_fulfillment_status_of_order(cls, extra_params: dict, order_id: str) -> dict:
        client = cls._initialize_session(extra_params)
        order = client.Orders.get(order_id)
        return {"order_id": order_id, "fulfillment_status": order.status}
