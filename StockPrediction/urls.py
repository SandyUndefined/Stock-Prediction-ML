from django.urls import path
from . import views

urlpatterns = [
    path("", views.greet, name='greet'),
    path("index/", views.index, name='Stock Prediction'),
    path("prediction/", views.prediction, name='Prediction')
]
