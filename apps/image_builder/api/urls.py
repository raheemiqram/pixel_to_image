from django.urls import path
from . import views

app_name = "image_builder_api"

urlpatterns = [
    path(
        "generate_image/",
        views.GenerateImage.as_view(),
        name="generate_image",
    ),
    path(
        "generated_image_list/<int:pk>/",
        views.GeneratedImageList.as_view(),
        name="generate_image-list",
    ),
]
