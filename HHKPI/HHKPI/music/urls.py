from django.urls import path

from . import views

urlpatterns = [
    #/music/ID_key
    path('<int:album_id>/', views.chitiet, name='chitiet'),
    path('<int:album_id>/detail', views.detail, name='detail'),
    # ex: /polls/
    path('', views.index, name='index'),
]




















































