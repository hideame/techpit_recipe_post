from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, TemplateView, UpdateView

from recipe.forms import RecipeForm
from recipe.models import Recipe


class StaffroomMixin(LoginRequiredMixin):
    login_url = reverse_lazy("login")


class StaffroomTemplateView(StaffroomMixin, TemplateView):
    template_name = "staffroom/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["recipe_list"] = Recipe.objects.filter(user=self.request.user).prefetch_related("comment_set")
        else:
            context["recipe_list"] = None
        return context


class RecipeCreateView(StaffroomMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipe/recipe_form.html"
    # fields = ["title", "content", "description", "image"]
    success_url = reverse_lazy("recipe:index")

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.POST.dict()
        data["user"] = user.id
        form = RecipeForm(data=data, files=request.FILES)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, "保存しました")
        return super().form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, "保存できませんでした")
        return super().form_invalid(form)


class RecipeUpdateView(StaffroomMixin, UpdateView):
    model = Recipe
    template_name = "recipe/recipe_form.html"
    fields = ["title", "content", "description", "image"]

    def get_success_url(self):
        pk = self.kwargs.get("pk")
        return reverse("recipe:detail", kwargs={"pk": pk})

    def form_valid(self, form):
        messages.success(self.request, "更新しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "更新できませんでした")
        return super().form_invalid(form)


class RecipeDeleteView(StaffroomMixin, DeleteView):
    model = Recipe
    template_name = "recipe/recipe_confirm_delete.html"
    success_url = reverse_lazy("recipe:index")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "削除しました")
        return super().delete(request, *args, **kwargs)
