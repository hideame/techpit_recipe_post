from django.urls import include, path

from ..views import StaffroomTemplateView

app_name = "staffroom"

urlpatterns = [
    path("", StaffroomTemplateView.as_view(), name="index"),
    path("recipe/", include("staffroom.urls.recipe", namespace="recipe")),
]
