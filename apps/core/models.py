from django.db import models
from simple_history.models import HistoricalRecords
from apps.core.middleware import get_current_authenticated_user
from apps.users.models import User


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey(
        User,
        null=True,
        related_name="created_%(app_label)s_%(class)s",
        on_delete=models.SET_NULL,
    )
    updated_by = models.ForeignKey(
        User,
        null=True,
        related_name="updated_%(app_label)s_%(class)s",
        on_delete=models.SET_NULL,
    )
    history = HistoricalRecords(inherit=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.created_by = get_current_authenticated_user()
        self.updated_by = get_current_authenticated_user()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True