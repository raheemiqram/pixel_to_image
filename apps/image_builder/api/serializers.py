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

    class Meta:
        model = ReConstructImage
        fields = ("id", "reconstruct_image", "created_by", "created", 'width', 'height')

    def get_width(self, obj):
        return obj.reconstruct_image.width

    def get_height(self, obj):
        return obj.reconstruct_image.height


class OriginalImageSerializer(ModelSerializer):
    class Meta:
        model = OriginalImage
        fields = "__all__"
