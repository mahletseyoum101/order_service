
from django.test import TestCase
from .models import Order

class OrderModelTest(TestCase):

    def setUp(self):
        Order.objects.create(item_id="123", quantity=2, customer_name="John Doe")

    def test_order_creation(self):
        order = Order.objects.get(item_id="123")
        self.assertEqual(order.customer_name, "John Doe")