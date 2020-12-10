from django.db import models

# Create your models here.


class lists_container(models.Model):
    store = models.CharField(max_length=500)

    def __str__(self):
        return self.store
