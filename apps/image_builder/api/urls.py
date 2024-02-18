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
        "original_image_list/",
        views.OriginalImageList.as_view(),
        name="original_image_list",
    ),
    path(
        "generated_image_list/<int:pk>/",
        views.GeneratedImageList.as_view(),
        name="generate_image-list",
    ),
]
