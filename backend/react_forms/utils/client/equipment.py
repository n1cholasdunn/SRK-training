from rest_framework.request import Request
from rest_framework.response import Response
from common.utils.client_serializers import ClientEquipmentSerializer
from common.models.client_models import ClientEquipment
from django.shortcuts import get_object_or_404
from rest_framework import status


def get_equipment(request: Request) -> Response:
    user = request.user
    equipment = get_object_or_404(ClientEquipment, trainee=user)
    serializer = ClientEquipmentSerializer(equipment)
    return Response(serializer.data)


def get_equipment_by_id(request: Request, pk: int) -> Response:
    equipment = get_object_or_404(ClientEquipment, pk=pk)
    serializer = ClientEquipmentSerializer(equipment)
    return Response(serializer.data)


def create_equipment(request: Request) -> Response:
    serializer = ClientEquipmentSerializer(
        data=request.data, context={"request": request}
    )
    if serializer.is_valid():
        serializer.save(trainee=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def update_equipment(request: Request, pk: int) -> Response:
    try:
        equipment = ClientEquipment.objects.get(pk=pk, trainee=request.user)
    except ClientEquipment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ClientEquipmentSerializer(
        equipment, data=request.data, partial=request.method == "PATCH"
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_equipment(request: Request, pk: int) -> Response:
    try:
        equipment = ClientEquipment.objects.get(pk=pk, trainee=request.user)
    except ClientEquipment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    equipment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
