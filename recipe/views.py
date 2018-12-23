from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render

from recipe.models import Recipe
from recipe.forms import EditForm  # TODO use edit form


class AuthorRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != self.request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class SaveWithAuthorMixin(object):
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

def index(request):
    '''View a list of all (selected) recipes'''

    all_recipes = Recipe.objects.all()

    return render(request, 'recipe/list.html', {
        'recipes': all_recipes
    })


def view(request, pk):
    '''View a recipe'''
    return render(request, 'recipe/view.html', {
        'recipe': Recipe.objects.get(pk=pk)
    })


class RecipeAdd(PermissionRequiredMixin, SaveWithAuthorMixin, CreateView):
    model = Recipe
    fields = ['name', 'description']
    success_url = '/'

    permission_required = 'recipe.add_recipe'


class RecipeUpdate(PermissionRequiredMixin, AuthorRequiredMixin, SaveWithAuthorMixin, UpdateView):
    model = Recipe
    fields = ['name', 'description']
    success_url = '/'

    permission_required = 'recipe.change_own_recipe'
