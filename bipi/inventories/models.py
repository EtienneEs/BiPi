from django.db import models
from model_utils.models import TimeStampedModel
from ..products.models import Product


class Inventory(TimeStampedModel):
    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(
        null=False,
        blank=False,
        default=0
    )

    def __str__(self):
        return f'Inventory: [{self.id}] {self.product} {self.quantity}'
