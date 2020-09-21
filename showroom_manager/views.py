from rest_framework import viewsets

from showroom_manager.models import Showroom
from showroom_manager.serializer import ShowroomSerializer


class ShowroomViewset(viewsets.ModelViewSet):
    queryset = Showroom.objects.all()
    serializer_class = ShowroomSerializer
