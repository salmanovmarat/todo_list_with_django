from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('delete/<list_id>:int', delete, name = "delete"),
    path('uncross/<list_id>:int', uncross, name='uncross'),
    path('cross_of/<list_id>:int', cross_of, name = "cross_of"),
    path('edit/<list_id>:int', edit, name='edit')
]