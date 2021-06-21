from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('city/', views.city, name='city'),
    path('city/<int:city_id>', views.city_update, name='city_update'),
]
