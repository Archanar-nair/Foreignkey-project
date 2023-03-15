from django.db import models

# Create your models here.
class course(models.Model):
    course_name=models.CharField(max_length=255)
    fee=models.IntegerField()
    def __str__ (self):
        return self.course_name

class student(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    address=models.CharField(max_length=255)
    date=models.DateField()
    def __str__ (self):
        return self.name
