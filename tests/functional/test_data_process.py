from django.core.files import File
from django.test import TestCase
from apps.image_builder.models import OriginalImage


class TestDataProcess(TestCase):
    def setUp(self):
        file_path = "tests/data/img.csv"
        with open(file_path, "rb") as f:
            file = File(f)
            original_image = OriginalImage()
            original_image.csv_file.save('file.txt', file, save=True)

    def test_data_process(self):
        self.assertEqual(OriginalImage.objects.count(), 1)
        img_csv = OriginalImage.objects.first()
        self.assertFalse(img_csv.original_image.name)
        # lets do the data process
        img_csv.data_process(commit=True)

        self.assertTrue(img_csv.original_image.name)  # image is generate successfully
        self.assertEqual(img_csv.original_width, 200)
        self.assertEqual(img_csv.original_height, 5460)
        self.assertEqual(img_csv.resized_width, 150)
        self.assertEqual(img_csv.resized_height, 4095)
        self.assertEqual(img_csv.minimum_depth, 9000.1)
        self.assertEqual(img_csv.maximum_depth, 9546.0)
