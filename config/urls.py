from django.contrib import admin
from django.urls import path

from lib.views import IndexTemplateView
from recipe.views import RecipeListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("recipe", RecipeListView.as_view(), name="recipe-index"),
    path("", IndexTemplateView.as_view(), name="index"),
]
