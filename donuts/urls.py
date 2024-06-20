from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from donuts import views


urlpatterns = [
    path('donuts/', views.DonutListView.as_view(), name='list_donut'),
    path('donuts/create/', views.DonutCreateView.as_view(), name='create_donut'),
    path('donuts/<int:pk>/update/', views.DonutUpdateView.as_view(), name='update_donut'),
    path('donuts/<int:pk>/detail/', views.DonutDetailView.as_view(), name='detail_donut'),
    path('donuts/<int:pk>/delete/', views.DonutDeleteView.as_view(), name='delete_donut'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)