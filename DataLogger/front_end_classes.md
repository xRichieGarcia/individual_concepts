# --- using django to design front of data logging application

from django.db import models

class Device(models.Model):
  device_id
  online_time

class Logs(models.Model):
  device = models.ForeignKey(Device, 
on_delete=models.CASCADE)
  log_data 


