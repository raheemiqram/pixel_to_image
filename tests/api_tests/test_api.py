from django.core.files import File
from django.urls import reverse
from rest_framework.test import APITestCase

from apps.image_builder.models import OriginalImage, ReConstructImage


class Tests(APITestCase):
    def setUp(self) -> None:
        super().setUp()
        file_path = "tests/data/img.csv"
        with open(file_path, "rb") as f:
            file = File(f)
            original_image = OriginalImage()
            original_image.csv_file.save('file.txt', file, save=True)

        original_image.data_process(commit=True)
        self.original_image = original_image

    def test_image_builder_api(self):
        self.assertEqual(ReConstructImage.objects.count(), 0)
        response = self.client.post(
            reverse("image_builder_api:generate_image"),
            data={
                "original_image_id": self.original_image.id,
                "rgb_color": "(0,0,250)",
                "depth_min": 9000,
                "depth_max": 9100
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ReConstructImage.objects.count(), 1)

        response = self.client.get(
            reverse("image_builder_api:generate_image-list", kwargs={"pk": self.original_image.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
