from django.urls import path
from . import views

urlpatterns = [
    path('', views.estimatorJson),
    path('json', views.estimatorJson),
    path('xml', views.estimatorXml),
    path('log', views.log)
]