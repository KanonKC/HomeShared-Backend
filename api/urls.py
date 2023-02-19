from django.urls import path
from .views import packet
urlpatterns = [
    path('packets',packet.create_packet),
    path('packets/<int:packet_id>',packet.manage_packet),
]