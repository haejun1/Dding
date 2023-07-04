from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gongmoCreate/", views.gongmoCreate, name="gongmoCreate"),
    path("<int:pk>/", views.gongmoDetail, name="gongmoDetail"),
    path("<int:pk>/teamCreate/", views.teamCreate, name="teamCreate"),
]