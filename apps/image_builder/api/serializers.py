import base64

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from apps.image_builder.models import ReConstructImage, OriginalImage


class GenerateImageSerializer(serializers.Serializer):
    original_image_id = serializers.IntegerField(required=True)
    rgb_color = serializers.CharField(max_length=20, required=False)
    depth_min = serializers.DecimalField(required=True, decimal_places=3, max_digits=12)
    depth_max = serializers.DecimalField(required=True, decimal_places=3, max_digits=12)


class GeneratedImageSerializer(ModelSerializer):
    width = serializers.SerializerMethodField()
    height = serializers.SerializerMethodField()
    image_binary = serializers.SerializerMethodField()

    class Meta:
        model = ReConstructImage
        fields = ("id", "reconstruct_image", "created_by", "created", 'width', 'height', 'image_binary')

    def get_width(self, obj):
        return obj.reconstruct_image.width

    def get_height(self, obj):
        return obj.reconstruct_image.height

    def get_image_binary(self, obj):
        try:
            # Open the image file
            with open(obj.reconstruct_image.path, "rb") as img_file:
                # Encode the binary image data in Base64
                image_data_base64 = base64.b64encode(img_file.read())
                return image_data_base64.decode("utf-8")  # Convert to UTF-8 for JSON serialization
        except Exception as e:
            # Handle any exceptions that may occur during image processing
            print(f"Error processing image: {e}")

        return None


class OriginalImageSerializer(ModelSerializer):
    class Meta:
        model = OriginalImage
        fields = "__all__"
