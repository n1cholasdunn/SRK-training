from common.utils.client_serializers import (
    ClientProgramInfoSerializer,
)
from common.models.client_models import ClientProgramInfo
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response


def get_program(request):
    user = request.user
    program = get_object_or_404(ClientProgramInfo, trainee=user)
    serializer = ClientProgramInfoSerializer(program)
    return Response(serializer.data)


def create_program(request):
    serializer = ClientProgramInfoSerializer(
        data=request.data, context={"request": request}
    )
    if serializer.is_valid():
        serializer.save(trainee=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def update_program(request, pk):
    try:
        program = ClientProgramInfo.objects.get(pk=pk, trainee=request.user)
    except ClientProgramInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ClientProgramInfoSerializer(
        program, data=request.data, partial=request.method == "PATCH"
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_program(request, pk):
    try:
        program = ClientProgramInfo.objects.get(pk=pk, trainee=request.user)
    except ClientProgramInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    program.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
