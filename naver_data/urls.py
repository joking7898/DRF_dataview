from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.NaverDataView.as_view(), name='data_view'),
]
