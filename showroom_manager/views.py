from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.response import Response

from showroom_manager.models import Car
from showroom_manager.serializer import ShowroomSerializer

car_id = openapi.Parameter('car_id', in_=openapi.IN_QUERY,
                           type=openapi.TYPE_INTEGER)

FETCH_CAR_SUCCESS = '''{{
    "id": <showroom id>, 
    "name": <showroom name>,
    "location": <showroom location>,
    "car": [
        {
            "model_no": <car model no>,
            "model_name": <car model name>,
            "showroom": <showroom no>
        }
    ]
}}'''


class ShowroomViewset(viewsets.ModelViewSet):
    serializer_class = ShowroomSerializer

    def get_queryset(self):
        # fetch specific showroom details from car id
        car_id = self.request.query_params.get('car_id')
        car = Car.objects.get(id=car_id)
        return car.showroom

    @swagger_auto_schema(
        operation_description="give car id to get showroom details",
        manual_parameters=[car_id],
        responses={200: FETCH_CAR_SUCCESS}

    )
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ShowroomSerializer(queryset)
        return Response(serializer.data)
