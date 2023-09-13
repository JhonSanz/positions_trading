from django.db import models
import uuid

class AbstractModel(models.Model):
    id = models.UUIDField(default=uuid.uuid1, unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        ordering = ["-created_at", "-updated_at"]
