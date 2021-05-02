from django.db import models
from model_utils.models import TimeStampedModel


class Product(TimeStampedModel):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return f'Product: {self.name}'
