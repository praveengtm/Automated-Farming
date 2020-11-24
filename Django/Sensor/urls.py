from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "home"),
    path('more/<int:sampleindex>',views.more,name = "more"),
]