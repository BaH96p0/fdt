from django.db import models
# Create your models here.



class Grade(models.Model):
    grade = models.IntegerField( primary_key=True)


class Lesson(models.Model):
    lesson = models.CharField(max_length=20, primary_key=True)


class Student(models.Model):
    name = models.CharField(max_length=20)
    surname = models.TextField(max_length=30)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)



