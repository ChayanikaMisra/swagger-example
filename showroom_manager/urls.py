from django.urls import path, include
from rest_framework.routers import DefaultRouter

from showroom_manager.views import ShowroomViewset

router = DefaultRouter()
router.register(r'', ShowroomViewset,basename='showroom')

urlpatterns = [
    path('', include(router.urls)),
]