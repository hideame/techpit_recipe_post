from django.contrib import admin
from django.urls import path

from lib.views import IndexTemplateView
from recipe.views import RecipeCreateView, RecipeListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("recipe", RecipeListView.as_view(), name="recipe-index"),
    path("recipe/create", RecipeCreateView.as_view(), name="recipe-create"),
    path("", IndexTemplateView.as_view(), name="index"),
]
