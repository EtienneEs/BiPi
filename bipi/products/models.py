from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from djmoney.models.fields import MoneyField
from ..accounts.models import Organization


class Product(TimeStampedModel):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return f'Product: {self.name}'

    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'pk': self.pk})


class Price(TimeStampedModel):
    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    organization = models.ForeignKey(
        Organization,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    price = MoneyField(
        max_digits=14,
        decimal_places=2,
        default_currency='EUR'
    )

    class Meta:
        unique_together = (('product', 'organization'), )

    def __str__(self):
        return f'{self.organization} - {self.product} {self.price}'

    def get_absolute_url(self):
        return reverse('products:price_detail', kwargs={'pk': self.pk})
