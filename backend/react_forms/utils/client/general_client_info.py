from common.utils.client_serializers import GeneralClientInfoSerializer
from common.models.client_models import GeneralClientInfo
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response


def get_general_client_info(request):
    user = request.user
    general_client_info = get_object_or_404(GeneralClientInfo, trainee=user)
    serializer = GeneralClientInfoSerializer(general_client_info)
    return Response(serializer.data)


def create_general_client_info(request):
    serializer = GeneralClientInfoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(trainee=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def update_general_client_info(request, pk):
    try:
        general_client_info = GeneralClientInfo.objects.get(pk=pk, trainee=request.user)
    except GeneralClientInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = GeneralClientInfoSerializer(
        general_client_info, data=request.data, partial=request.method == "PATCH"
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_general_client_info(request, pk):
    try:
        general_client_info = GeneralClientInfo.objects.get(pk=pk, trainee=request.user)
    except GeneralClientInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    general_client_info.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
