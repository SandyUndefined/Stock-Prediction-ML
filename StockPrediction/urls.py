from django.urls import path
from . import views

urlpatterns = [
    path("", views.greet, name='greet'),
    path("index.html", views.index, name='Stock Prediction'),
    path("Prediction/", views.prediction, name='Prediction')
]
