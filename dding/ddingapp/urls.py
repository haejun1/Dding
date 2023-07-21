from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gongmoCreate/", views.gongmoCreate, name="gongmoCreate"),
    path("<int:gongmoPk>/", views.gongmoDetail, name="gongmoDetail"),
    path("<int:gongmoPk>/gongmoDelete/", views.gongmoDelete, name="gongmoDelete"),
    path("<int:gongmoPk>/teamCreate/", views.teamCreate, name="teamCreate"),
    path("<int:gongmoPk>/<int:teamPk>/", views.teamDetail, name="teamDetail"),
    path("<int:gongmoPk>/<int:teamPk>/teamDelete/", views.teamDelete, name="teamDelete"),
    path('<int:gongmoPk>/<int:teamPk>/teamJoin/', views.teamJoin, name='teamJoin'),
    path('mypage/<int:user_id>/', views.mypage, name='mypage'),
    path('<int:teamPk>/bookmark/', views.bookmark, name='bookmark'),
]