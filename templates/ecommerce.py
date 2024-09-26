from abc import ABC, abstractmethod


class EcommerceActionList(ABC):

    @classmethod
    @abstractmethod
    def get_customer_by_email(cls, extra_params: dict, customer_id: str) -> dict:
        pass

    @classmethod
    @abstractmethod
    def get_customer_by_phone(cls, extra_params: dict, order_id: str) -> dict:
        pass

    @classmethod
    @abstractmethod
    def get_most_recent_customer_orders(cls, extra_params: dict, customer_id: str, limit: int = 10) -> dict:
        pass

    @classmethod
    @abstractmethod
    def cancel_order(cls, extra_params: dict, order_id: str) -> dict:
        pass

    @classmethod
    @abstractmethod
    def create_refund(cls, extra_params: dict, order_id: str) -> dict:
        pass

    @classmethod
    @abstractmethod
    def get_order_by_order_number(cls, extra_params: dict, order_id: str) -> dict:
        pass

    @classmethod
    @abstractmethod
    def get_fulfillment_status_of_order(cls, extra_params: dict, order_id: str) -> dict:
        pass