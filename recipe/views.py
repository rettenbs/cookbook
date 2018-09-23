from django.views.generic.edit import UpdateView
from django.shortcuts import render

from recipe.models import Recipe
from recipe.forms import EditForm


def index(request):
    '''View a list of all (selected) recipes'''
    
    all_recipes = Recipe.objects.all()
    
    return render(request, 'recipe/list.html', {
        'recipes': all_recipes
    })


def view(request, id):
    '''View a recipe'''
    return render(request, 'recipe/view.html', {
        'recipe': Recipe.objects.get(pk=id)
    })
    


class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['name', 'description']
    success_url = '/'
