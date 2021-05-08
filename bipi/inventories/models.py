from django.db import models
from django.urls import reverse

from model_utils.models import TimeStampedModel

from ..products.models import Product


class Stock(TimeStampedModel):
    """Finished goods """
    product = models.OneToOneField(
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
        return f'Stock: {self.product.name}'

    def get_absolute_url(self):
        return reverse('inventories:stock_detail', kwargs={'pk': self.pk})