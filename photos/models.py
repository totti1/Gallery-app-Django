from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    street = models.CharField(max_length =30)

    def __str__(self):
        return self.street

class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    @classmethod
    def search_by_name(cls,search_term):
        category = cls.objects.filter(name__icontains=search_term)
        return category

class Image(models.Model):
    title = models.CharField(max_length =60)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/', blank=True)

    def __str__(self):
        return self.title

    @classmethod
    def search_by_category(cls,search_term):
        news = cls.objects.filter(category=search_term)
        return news
