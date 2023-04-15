from django.urls import path
from ProductMaster import views

urlpatterns = [
    path('', views.index, name = 'ProductMasterIndex'),
    path('other/', views.other, name = 'ProductMasterOther'),
    path('MaterialMaster/', views.MaterialMasterView, name = 'MaterialMaster'),
]
