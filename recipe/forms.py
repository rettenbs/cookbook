from django import forms
from django.utils.translation import gettext as _

from recipe.models import Recipe

class EditForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description']
