from django.db import models
from model_utils.models import TimeStampedModel


class Organization(TimeStampedModel):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self):
        return f'Organization: {self.name}'


class Account(TimeStampedModel):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True
    )
    address = models.TextField(
        null=True,
        blank=True
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    def __str__(self):
        return f'Account: {self.name} ({self.organization})'
