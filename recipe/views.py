from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Recipe


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe/recipe_list.html"


class RecipeCreateView(CreateView):
    model = Recipe
    template_name = "recipe/recipe_form.html"
    fields = [
        "title",
        "content",
        "description",
        "image",
    ]
    success_url = reverse_lazy("recipe:index")

    def form_valid(self, form):
        messages.success(self.request, "保存しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "保存できませんでした")
        return super().form_invalid(form)


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe/recipe_detail.html"


class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name = "recipe/recipe_form.html"
    fields = [
        "title",
        "content",
        "description",
        "image",
    ]

    def get_success_url(self):
        pk = self.kwargs.get("pk")
        return reverse("recipe:detail", kwargs={"pk": pk})

    def form_valid(self, form):
        messages.success(self.request, "更新しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "更新できませんでした")
        return super().form_invalid(form)


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = "recipe/recipe_confirm_delete.html"
    success_url = reverse_lazy("recipe:index")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "削除しました")
        return super().delete(request, *args, **kwargs)
