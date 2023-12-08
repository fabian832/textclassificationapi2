from django.urls import path, include
from .views import TextClassification
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('api/text-classification/', TextClassification.as_view()),
    path('', include(router.urls))
]
