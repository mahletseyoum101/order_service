

from django.db import models

class Order(models.Model):
    item_id = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    customer_name = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer_name}"