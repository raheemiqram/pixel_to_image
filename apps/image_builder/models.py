import io
from django.core.files.base import ContentFile
from django.core.validators import FileExtensionValidator
from apps.core.models import BaseModel
from django.db import models
from PIL import Image, ImageOps
import pandas as pd


class OriginalImage(BaseModel):
    csv_file = models.FileField(upload_to='csv_files/',
                                validators=[FileExtensionValidator(allowed_extensions=["csv"])], )
    description = models.CharField(max_length=255, blank=True)
    original_image = models.ImageField(upload_to='original_images/', blank=True)
    original_width = models.IntegerField(blank=True, null=True)
    original_height = models.IntegerField(blank=True, null=True)
    resized_image = models.ImageField(upload_to='resized_image/', blank=True)
    resized_width = models.IntegerField(blank=True, null=True)
    resized_height = models.IntegerField(blank=True, null=True)
    error_message = models.TextField(blank=True)
    minimum_depth = models.IntegerField(blank=True, null=True)
    maximum_depth = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.csv_file.name

    def data_process(self, depth_min=None, depth_max=None, rgb_color=None, commit=False):
        # Load CSV file into DataFrame
        df = pd.read_csv(self.csv_file.path)

        # Find min and max depth
        min_depth = depth_min or df['depth'].min()
        max_depth = depth_max or df['depth'].max()

        # Filter data based on depth
        filtered_data = df[(df['depth'] >= float(min_depth)) & (df['depth'] <= float(max_depth))]

        # Extract pixel data
        pixel_data = filtered_data.drop('depth', axis=1).values

        # Convert pixel data to uint8
        pixel_data = pixel_data.astype('uint8')

        # Reshape pixel data to image dimensions (assuming it's grayscale)
        height, width = pixel_data.shape

        # Convert pixel data to an image:
        # - pixel_data: A numpy array containing the pixel values of the image.
        # - reshape(height, width): Reshape the pixel data array to match the height and width of the image.
        # - Image.fromarray(): Create a new image from the pixel data array.

        image = Image.fromarray(pixel_data.reshape(height, width))  # Assuming pixel data is in the range 0-255

        # Apply custom color map
        if rgb_color:
            # Apply colorization to the image:
            # - image.convert('L'): Convert the original image to grayscale. ('L' mode represents grayscale images)
            # - ImageOps.colorize(): Apply colorization to the grayscale image.
            # - black='black': Define the color for the darkest parts of the image,
            #                  typically where the grayscale values are closest to 0.
            #                  In this case, it's set to 'black', meaning those areas will be colored black.
            # - white=rgb_color: Define the color for the lightest parts of the image, typically where the grayscale
            #                    values are closest to 255 'rgb_color' holds an RGB color value,
            #                    which means those areas will be colored with the specified RGB color.

            image = ImageOps.colorize(image.convert('L'), black='black', white=rgb_color)

        if not commit:
            return image

        # Resize the image while preserving the aspect ratio
        aspect_ratio = width / height
        new_width = 150
        new_height = int(new_width / aspect_ratio)
        resized_image = image.resize((new_width, new_height))

        self.original_image.save('original.jpg', self.handle_image_upload(image), save=True)
        self.resized_image.save('resized.jpg', self.handle_image_upload(resized_image), save=True)

        self.original_width = width
        self.original_height = height
        self.resized_width = new_width
        self.resized_height = new_height
        self.minimum_depth = min_depth
        self.maximum_depth = max_depth
        self.save()

    def handle_image_upload(self, image):
        # Save the PIL image to a BytesIO buffer
        image_io = io.BytesIO()
        image.save(image_io, format='JPEG')  # Change format as needed
        image_io.seek(0)
        # Create a ContentFile from the BytesIO buffer
        content_file = ContentFile(image_io.read(), name='convert_image.jpg')  # Change name as needed
        return content_file


class ReConstructImage(BaseModel):
    original_image = models.ForeignKey(OriginalImage, on_delete=models.CASCADE)
    reconstruct_image = models.ImageField(upload_to='reconstruct_images/')
