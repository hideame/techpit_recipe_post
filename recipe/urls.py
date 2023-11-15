from django.urls import path

from recipe.views import RecipeCreateView, RecipeDeleteView, RecipeDetailView, RecipeListView, RecipeUpdateView

app_name = "recipe"

urlpatterns = [
    path("", RecipeListView.as_view(), name="index"),
    path("create", RecipeCreateView.as_view(), name="create"),
    path("<int:pk>", RecipeDetailView.as_view(), name="detail"),
    path("<int:pk>/update", RecipeUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", RecipeDeleteView.as_view(), name="delete"),
]
