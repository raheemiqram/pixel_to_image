from django.urls import path

from apps.image_builder.views import UploadCSV, CSVList, ImageBuilder

urlpatterns = [
    path('list/', CSVList.as_view(), name='csv_list'),
    path('upload/', UploadCSV.as_view(), name='csv_upload'),
    path('build/<int:pk>/', ImageBuilder.as_view(), name='image_builder'),
]
