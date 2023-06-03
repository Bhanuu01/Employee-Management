from django.db import models

# Create your models here.

class ClientInfo(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=10)

    class Meta:
        verbose_name = ("ClientInfo")
        verbose_name_plural = ("ClientInfo")
        
    def __str__(self):
        return self.name

