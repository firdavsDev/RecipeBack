from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class RoleChoice(models.TextChoices):
    pharmacy_owner = "pharmacy_owner", _("Pharmacy Owner")
    pharmacist_admin = "pharmacist_admin", _("Pharmacist Admin")
    pharmacist = "pharmacist", _("Pharmacist")
    user = "user", _("User")
    super_admin = "super_admin", _("Super Admin")
