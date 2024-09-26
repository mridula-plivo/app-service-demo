from django.core.management.base import BaseCommand

from name_later import execute_action


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        ORG_ID = 1
        APP_ID = 3
        ORG_APP_ID = 3
        ORDER_NUMBER = 1221
        PHONE_NUMBER = '+919877892588'

        print("Incoming call: Customer calls\n\n")
        print("Phone number is " + PHONE_NUMBER + "\n\n")
        print("AI customer details by phone\n\n")
        customer_details = execute_action("get_customer_by_phone", ORG_ID, APP_ID, phone=PHONE_NUMBER)
        print(customer_details)
        print("\n\n")
        print(f"Customer wants to cancel order number {ORDER_NUMBER}\n\n")
        response = execute_action("cancel_order", ORG_ID, APP_ID, order_id=ORDER_NUMBER)
        print(response)