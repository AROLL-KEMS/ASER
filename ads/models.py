from django.db import models

# Create your models here.
class contacts(models.Model):
    name = models.CharField()
    email = models.EmailField()
    phone = models.CharField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.email} - {self.date}"
