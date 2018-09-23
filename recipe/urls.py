from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.RecipeAdd.as_view(), name='add'),
    path('view/<int:pk>', views.view, name='view'),
    path('edit/<int:pk>', views.RecipeUpdate.as_view(), name='edit')
]
