from django.urls import path
from APIs import views
urlpatterns = [
    path('', views.search),
]