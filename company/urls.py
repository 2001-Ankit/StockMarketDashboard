from django.urls import path
from .views import *
urlpatterns = [
    path('',CompanyView.as_view(),name='company'),
]

