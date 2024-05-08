from django.db import models
from django.db.models import PROTECT
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Driver(models.Model):
    rut = models.CharField(_("RUT"), max_length=9, primary_key=True)
    name = models.CharField(_("Name"), max_length=50)
    last_name = models.CharField(_("Last name"), max_length=50)
    active = models.BooleanField(_("Active"), default=False)
    created_at = models.DateTimeField(_("Created at"), default=timezone.now, editable=False)
    vehicle = models.OneToOneField(
        "Vehicle",
        verbose_name=_("Vehicle"),
        related_name="driver",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.rut

    class Meta:
        verbose_name = _("Driver")
        verbose_name_plural = _("Drivers")
        ordering = ["rut"]

class Vehicle(models.Model):
    registration_plate = models.CharField(_("Registration plate"), max_length=6, primary_key=True)
    brand = models.CharField(_("Brand"), max_length=20)
    model = models.CharField(_("Model"), max_length=20)
    year = models.DateField(_("Year"))
    active = models.BooleanField(_("Active"), default=False)
    created_at = models.DateTimeField(_("Created at"), default=timezone.now, editable=False)

    def __str__(self):
        return self.registration_plate

    class Meta:
        verbose_name = _("Vehicle")
        verbose_name_plural = _("Vehicles")
        ordering = ["registration_plate"]

class AccountingRegistry(models.Model):
    date_of_purchase = models.DateField(_("Date of purchase"))
    price = models.FloatField(_("Price"))
    vehicle = models.OneToOneField(
        "Vehicle",
        verbose_name=_("Vehicle"),
        related_name="accounting",
        on_delete=PROTECT
    )

    def __str__(self):
        return self.vehicle.registration_plate

    class Meta:
        verbose_name = _("Accounting Registry")
        verbose_name_plural = _("Accounting Registries")
        ordering = ["date_of_purchase"]
