from django.contrib import admin
from donuts.models import Donut

@admin.register(Donut)
class DonutAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo')
    search_fields = ('nome', 'tipo')

