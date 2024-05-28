from django.db import models

# Create your models here.

class contact(models.Model):
  name=models.CharField(max_length=100)
  email=models.EmailField()
  phone=models.CharField(max_length=30,null=True,blank=True)
  subject=models.CharField(max_length=500)
  message=models.TextField()
  created_at=models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    #return self.name
    return self.name + " " + self.email