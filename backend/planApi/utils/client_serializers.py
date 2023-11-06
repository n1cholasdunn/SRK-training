from planApi.models.common import BaseClientInfo
from planApi.models.client_models import (
    ClientAvailability,
    ClientEquipment,
    ClientProgramInfo,
    DayAvailability,
    Equipment,
    GeneralClientInfo,
)
from rest_framework.serializers import ModelSerializer


class DayAvailabilitySerializer(ModelSerializer):
    class Meta:
        model = DayAvailability
        fields = "__all__"


class GeneralClientInfoSerializer(ModelSerializer):
    availabilities = DayAvailabilitySerializer(many=True, read_only=True)

    class Meta:
        model = GeneralClientInfo
        fields = "__all__"


class ClientAvailabilitySerializer(ModelSerializer):
    class Meta:
        model = ClientAvailability
        fields = "__all__"


class EquipmentSerializer(ModelSerializer):
    class Meta:
        model = Equipment
        fields = "__all__"


class ClientEquipmentSerializer(ModelSerializer):
    equipment = EquipmentSerializer()

    class Meta:
        model = ClientEquipment
        fields = "__all__"


class ClientProgramInfoSerializer(ModelSerializer):
    class Meta:
        model = ClientProgramInfo
        fields = "__all__"
