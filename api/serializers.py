
from rest_framework import serializers
from .models import *

class SharedPacketSerializers(serializers.ModelSerializer):
    class Meta:
        model = SharedPacket
        fields = "__all__"

    def create(self,validate_data):
        return SharedPacket.objects.create(**validate_data)

    def update(self,instance,validate_data):
        instance.message = validate_data.get('message',instance.message)
        instance.save()
        return instance