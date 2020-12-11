from rest_framework import serializers
from .models import popGraph

class PopSerializer(serializers.ModelSerializer):
    class Meta:
        model = popGraph
        fields = ('id', 'lyrics')