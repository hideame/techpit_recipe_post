from django.views.generic import CreateView, ListView

from .models import Recipe


class RecipeListView(ListView):
    model = Recipe


class RecipeCreateView(CreateView):
    model = Recipe
    fields = ["title", "content", "description"]
    success_url = "/"
