from django.contrib import admin

class EmailModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'assunto')
    search_fields = ('nome', 'email', 'assunto', 'telefone')
