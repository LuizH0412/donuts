from django.contrib import admin
from centos.models import Cento

@admin.register(Cento)
class CentoAdmin(admin.ModelAdmin):
    list_display = ('valor', 'quantidade', 'tipo')
    search_fields = ('quantidade', 'tipo')
