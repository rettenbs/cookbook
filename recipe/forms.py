from django import forms

from recipe.models import Recipe

class EditForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description']
