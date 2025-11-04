from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class ContactMessages(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=14, blank=True, null=True)
    message = models.TextField()
    
    def __str__(self):
        return self.fullname