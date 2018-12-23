from django.contrib.auth import get_user_model
from django.db import models


class Recipe(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)

    class Meta:
        permissions = (('change_own_recipe', 'Can change own recipe'),)
