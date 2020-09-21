from django.urls import path, include
from rest_framework.routers import DefaultRouter

from showroom_manager.views import ShowroomViewset

router = DefaultRouter()
router.register(r'', ShowroomViewset)

urlpatterns = [
    path('', include(router.urls)),
]
