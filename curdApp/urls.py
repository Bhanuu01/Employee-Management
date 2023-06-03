
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('add/',add_client,name='add'),
    path('edit/<int:id>/',edit_client,name='edit'),
    path('delete/<int:id>/',delete_client,name='delete'),
]