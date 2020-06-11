from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='Stock Prediction'),
    path("Prediction/", views.prediction, name='Prediction')
]
