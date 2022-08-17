from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    lname = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=15, default="")
    query = models.TextField()
    dateStump = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.name} Contacts you."
