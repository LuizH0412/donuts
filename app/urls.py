
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # URLs Donuts
    path('', include('donuts.urls')),

    # URLs Home
    path('', include('paginas.urls')),
]
