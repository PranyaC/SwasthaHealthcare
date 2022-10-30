from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Contact"

class Blog(models.Model):
    name=models.CharField(max_length=100)
    postdate=models.CharField(max_length=100)
    posttitle = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.posttitle + self.name
    class Meta:
        verbose_name_plural = "Blog"