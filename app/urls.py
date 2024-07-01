
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # URLs Donuts
    path('', include('donuts.urls')),

    # URLs Home
    path('', include('paginas.urls')),

    # URLs Cento
    path('', include('centos.urls')),

    # URLs Email
    path('', include('emails.urls'))
]
