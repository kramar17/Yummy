from django.urls import path
from .views import IndexView, manager

app_name = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('manager/', manager, name='manager'),
]