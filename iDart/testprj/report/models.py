from django.db import models

# Create your models here.

class Student(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    #age = models.IntegerField

    def __str__(self):
        return f" {self.firstname} {self.lastname}"


class Subject(models.Model):
    code = models.CharField(max_length=3,unique=True)
    name = models.CharField(max_length=32,blank=True)

    def __str__(self):
        return f" {self.code} {self.name}"

class Mark(models.Model):
    score = models.IntegerField()
    subject = models.ForeignKey(Subject,on_delete=models.PROTECT,related_name='marks')
    student = models.ForeignKey(Student,on_delete=models.SET_NULL,null=True,blank=True,related_name='marks')

    def __str__(self):
        return f"{self.score} {self.subject.code} {self.student.name}"
