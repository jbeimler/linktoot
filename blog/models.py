from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32)
    prefix = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return (f"{self.name}")

class Post(models.Model):
    data = models.TextField(max_length=400)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return(f"{self.data[:39]}…")
