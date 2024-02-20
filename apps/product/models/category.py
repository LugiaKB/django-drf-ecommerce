from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    class Meta:
        app_label = "product"

    name = models.CharField(max_length=100)
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name
