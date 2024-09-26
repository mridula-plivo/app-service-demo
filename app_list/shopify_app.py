import shopify

from templates.ecommerce import EcommerceActionList


class ShopifyActions(EcommerceActionList):
    @classmethod
    def _initialize_session(cls, extra_params: dict):
        shopify_session = shopify.Session(
            f"{extra_params['store_name']}.myshopify.com",
            '2024-04',
            extra_params['auth_token'],
        )
        shopify.ShopifyResource.activate_session(shopify_session)

    @classmethod
    def get_customer_by_email(cls,extra_params: dict, email: str) -> dict:
        cls._initialize_session(extra_params)
        customer = shopify.Customer.search(email=email)
        return customer[0].to_dict() if customer else {}

    @classmethod
    def get_customer_by_phone(cls,extra_params: dict, phone: str) -> dict:
        cls._initialize_session(extra_params)
        customers = shopify.Customer.search(phone=phone)
        return customers[0].to_dict() if customers else {}

    @classmethod
    def get_most_recent_customer_orders(cls,extra_params: dict, customer_id: str, limit: int = 10) -> dict:
        cls._initialize_session(extra_params)
        orders = shopify.Order.find(customer_id=customer_id, limit=limit, order="created_at DESC")
        return [order.to_dict() for order in orders]

    @classmethod
    def cancel_order(cls,extra_params: dict, order_id: str) -> dict:
        cls._initialize_session(extra_params)
        order = shopify.Order.find(name=order_id)[0]
        order.cancel()
        return {"success": True, "message": "Successfully cancelled order"}

    @classmethod
    def create_refund(cls,extra_params: dict, order_id: str) -> dict:
        cls._initialize_session(extra_params)
        order = shopify.Order.find(order_id)
        refund = shopify.Refund.create({
            "order_id": order.id,
            "refund_line_items": [{"line_item_id": item.id, "quantity": item.quantity} for item in order.line_items],
            "notify": True
        })
        return refund.to_dict() if refund else {}

    @classmethod
    def get_order_by_order_number(cls, extra_params: dict, order_number: str) -> dict:
        cls._initialize_session(extra_params)
        orders = shopify.Order.find(name=order_number)
        return orders[0].to_dict() if orders else {}

    @classmethod
    def get_fulfillment_status_of_order(cls,extra_params: dict, order_id: str) -> dict:
        cls._initialize_session(extra_params)
        order = shopify.Order.find(order_id)
        return {"order_id": order.id, "fulfillment_status": order.fulfillment_status}