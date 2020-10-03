from rest_framework import serializers

from showroom_manager.models import Showroom, Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Car
        fields = ['model_no', 'model_name', 'showroom']


class ShowroomSerializer(serializers.ModelSerializer):
    car = CarSerializer(source='car_set', many=True)

    class Meta:
        model = Showroom
        fields = ['id', 'name', 'location', 'car']
