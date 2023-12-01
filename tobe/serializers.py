from rest_framework import serializers
from .models import *


class TobeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tobe
        fields = '__all__'