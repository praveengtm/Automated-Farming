from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index, name = 'index'),
    path('more/<int:sample_id>',views.more,name = "more"),
]
