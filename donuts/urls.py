from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from donuts.views import CombinedListView, DonutDetailView


urlpatterns = [
    path('donuts/', CombinedListView.as_view(), name='list_donut'),
    path('donuts/<int:pk>/detail/', DonutDetailView.as_view(), name='detail_donut'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)