from planApi.models.client_models import (
    ClientAvailability,
    ClientEquipment,
    ClientProgramInfo,
    DayAvailability,
    Equipment,
    GeneralClientInfo,
)
from rest_framework.serializers import ModelSerializer


class GeneralClientInfoSerializer(ModelSerializer):
    class Meta:
        model = GeneralClientInfo
        fields = "__all__"


class DayAvailabilitySerializer(ModelSerializer):
    class Meta:
        model = DayAvailability
        fields = "__all__"


class ClientAvailabilitySerializer(ModelSerializer):
    monday = DayAvailabilitySerializer()
    tuesday = DayAvailabilitySerializer()
    wednesday = DayAvailabilitySerializer()
    thursday = DayAvailabilitySerializer()
    friday = DayAvailabilitySerializer()
    saturday = DayAvailabilitySerializer()
    sunday = DayAvailabilitySerializer()

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
