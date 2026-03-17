from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField()
    course = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.usn})"
