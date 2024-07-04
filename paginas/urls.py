from django.urls import path
from paginas import views


urlpatterns = [
    path('contato/', views.ContatoView.as_view(), name='contato'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('local/', views.LocalView.as_view(), name='local'),
]