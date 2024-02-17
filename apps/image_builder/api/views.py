import ast

from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.image_builder.api.serializers import GeneratedImageSerializer, GenerateImageSerializer
from apps.image_builder.models import ReConstructImage, OriginalImage
from drf_spectacular.utils import extend_schema


@extend_schema(request=GenerateImageSerializer)
class GenerateImage(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = (SessionAuthentication,)
    serializer = GenerateImageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer(data=request.data)
        is_serializer_valid = serializer.is_valid(raise_exception=True)

        if is_serializer_valid:
            data = serializer.validated_data
            rgb_color = data.get("rgb_color", None)
            if rgb_color:
                rgb_color = ast.literal_eval(rgb_color)
            depth_min = data.get("depth_min")
            depth_max = data.get("depth_max")
            original_image = get_object_or_404(OriginalImage, id=data.get("original_image_id"))
            try:
                image = original_image.data_process(depth_min=depth_min, depth_max=depth_max, rgb_color=rgb_color,
                                                    commit=False)
                content_image = original_image.handle_image_upload(image)
                construct_image = ReConstructImage.objects.create(original_image=original_image,
                                                                  reconstruct_image=content_image)
                return Response({"data": GeneratedImageSerializer(construct_image).data}, status=200)
            except Exception as e:
                return Response({"message": f"Build fail due to {e}"}, status=400)


class GeneratedImageList(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = GeneratedImageSerializer

    def get_queryset(self):
        original_image = OriginalImage.objects.get(id=7)
        return ReConstructImage.objects.filter(original_image=original_image)
