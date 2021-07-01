from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('photo/<str:pk>/',views.photos, name='photo'),

]
