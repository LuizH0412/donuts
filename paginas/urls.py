from django.urls import path
from paginas import views


urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('info/', views.InfoView.as_view(), name='quem_somos'),
    path('contato/', views.ContatoView.as_view(), name='contato'),
]