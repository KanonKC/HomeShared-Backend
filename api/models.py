from django.db import models

# Create your models here.
class SharedPacket(models.Model):
    # mac_address = models.CharField(max_length=17)
    packet_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=100000,blank=True,null=True)
    file = models.FileField(upload_to='file/',null=True,blank=True)
    time = models.DateTimeField(auto_now_add=True)