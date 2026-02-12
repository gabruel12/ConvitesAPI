from rest_framework import serializers
from .models import Convites

class ConvitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convites
        fields = '__all__'
        read_only_fields = ['remetente']
