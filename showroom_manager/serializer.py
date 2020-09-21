from rest_framework import serializers

from showroom_manager.models import Showroom


class ShowroomSerializer(serializers.ModelSerializer):
    car = CarSerializer
    class Meta:
        model = Showroom
        fields = ['id', 'name', 'location']

class CarSerializer(serializers.ModelSerializer):

