from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wish/create/', views.ItemCreate.as_view(), name='create'),
    path('wish/<int:pk>/delete/', views.ItemDelete.as_view(), name='delete')
]