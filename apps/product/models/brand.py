from django.db import models


class Brand(models.Model):
    class Meta:
        app_label = "product"

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
