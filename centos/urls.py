from django.urls import path
from centos import views


urlpatterns = [
    path('centos/', views.CentoListView.as_view(), name='list_cento'),
    path('centos/create/', views.CentoCreateView.as_view(), name='create_cento'),
    path('centos/<int:pk>/update/', views.CentoUpdateView.as_view(), name='update_cento'),
    path('centos/<int:pk>/detail/', views.CentoDetailView.as_view(), name='detail_cento'),
    path('centos/<int:pk>/delete/', views.CentoDeleteView.as_view(), name='delete_cento'),
]