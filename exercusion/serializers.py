from rest_framework import serializers
from .models import Execursion

class ExecursionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Execursion
        fields = "__all__"
        