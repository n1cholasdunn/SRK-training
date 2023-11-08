from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from rest_framework import status
import requests


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    serializer = CustomUserSerializer(request.user)
    try:
        return Response(serializer.data)
    except requests.RequestException as e:
        return Response(
            {"error": f"Failed to fetch perms from user: {str(e)}"},
            status=status.HTTP_400_BAD_REQUEST,
        )
