from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField()
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name','first_name']

    def get_absolute_url(self):
        return reverse('author_detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.first_name}, {self.last_name}'
    
class Blog(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['published_date']
        
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])
    
    def __str__(self):
        return self.name