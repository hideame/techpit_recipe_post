from django.contrib import admin
from django.urls import path

from recipe.views import RecipeListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RecipeListView.as_view(), name="index"),
]
