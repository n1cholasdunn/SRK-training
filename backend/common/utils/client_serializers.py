from common.models.common import BaseClientInfo
from common.models.client_models import (
    ClientAvailability,
    ClientEquipment,
    ClientProgramInfo,
    DayAvailability,
    Equipment,
    GeneralClientInfo,
)
from common.utils.base_serializer import BaseOwnerFieldSerializer
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField


class DayAvailabilitySerializer(ModelSerializer):
    class Meta:
        model = DayAvailability
        fields = "__all__"


class GeneralClientInfoSerializer(BaseOwnerFieldSerializer):
    availabilities = DayAvailabilitySerializer(many=True, read_only=True)

    class Meta(BaseOwnerFieldSerializer.Meta):
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


class ClientEquipmentSerializer(BaseOwnerFieldSerializer):
    equipment = EquipmentSerializer(many=True, required=False)

    class Meta(BaseOwnerFieldSerializer.Meta):
        model = ClientEquipment
        fields = "__all__"
        extra_kwargs = {"trainee": {"read_only": True}}

    def create(self, validated_data):
        equipment_data = validated_data.pop("equipment", [])
        client_equipment = ClientEquipment.objects.create(**validated_data)
        for equipment_item in equipment_data:
            eq, created = Equipment.objects.get_or_create(**equipment_item)
            client_equipment.equipment.add(eq)
        return client_equipment


class ClientProgramInfoSerializer(BaseOwnerFieldSerializer):
    class Meta(BaseOwnerFieldSerializer.Meta):
        model = ClientProgramInfo
        fields = "__all__"
        extra_kwargs = {"trainee": {"read_only": True}}
