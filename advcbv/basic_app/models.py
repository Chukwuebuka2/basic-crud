from django.db import models
from django.urls import reverse

# Create your models here.
class School (models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__ (self):
        return self.name

    def get_absolute_url(self):
        ''''This method helps us to redirect to another page when we have successfully created the view'''
        return reverse('basic_app:detail', kwargs={'pk':self.pk})
    

class Students(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey('School', related_name='students', on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name  