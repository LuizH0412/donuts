from django.urls import path
from centos import views


urlpatterns = [
    path('centos/', views.CentoListView.as_view(), name='list_cento'),
    path('centos/<int:pk>/detail/', views.CentoDetailView.as_view(), name='detail_cento'),
]