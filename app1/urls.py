from django.urls import path
from app1.views import *

app_name='app1'

urlpatterns=[
    path('app1first/',app1first,name='app1first')
]