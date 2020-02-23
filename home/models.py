from django.db import models
import uuid
# Create your models here.

class motd(models.Model):
    motd_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    time_created = models.DateTimeField(auto_now_add=True,auto_now=False)
    time_lastmodified = models.DateTimeField(auto_now=True)
    title=models.CharField(max_length = 50)
    content = models.TextField()
    def __str__(self):
        return self.title
    
