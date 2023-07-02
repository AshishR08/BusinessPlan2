from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name = 'home'),
    path('b1a65246-7154-4f7a-a973-f6f36cee92ac', views.whatsAppWebhook, name = 'whatsapp-webhook'),
]

#https://1bc8-102-113-29-160.ngrok-free.app/b1a65246-7154-4f7a-a973-f6f36cee92ac
# Token = 1234