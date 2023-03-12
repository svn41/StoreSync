from django.urls import path
from ProductMaster import views

urlpatterns = [
    path('', views.index, name = 'ProductMasterIndex'),
    path('users/', views.other, name = 'ProductMasterUsers'),
]
