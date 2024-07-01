from django.urls import path
from paginas import views


urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('local/', views.LocalView.as_view(), name='local'),
]