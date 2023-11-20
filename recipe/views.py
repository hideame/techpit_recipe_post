from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView

from comment.forms import CommentForm

from .models import Recipe


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe/recipe_list.html"

    def get_queryset(self):
        qs = Recipe.objects.all()
        keyword = self.request.GET.get("q")
        if keyword:
            qs = qs.filter(title__contains=keyword)
        return qs


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe/recipe_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["CommentForm"] = CommentForm(initial={"recipe": self.object})
        return context
