from django.db import models
from django.utils.text import slugify


# Create your models here.
class Company(models.Model):
    cname = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    website = models.URLField(max_length=100,blank=True)
    slug = models.SlugField(max_length=100,unique=True,blank=True,null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.cname
