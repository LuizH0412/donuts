from django.urls import path
from emails.views import EmailView


urlpatterns = [
    path('contato/', EmailView.as_view(), name='contato')
]