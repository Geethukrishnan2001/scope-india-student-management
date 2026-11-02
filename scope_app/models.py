from django.db import models

# Create your models here.
class Country(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class State(models.Model):

    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class City(models.Model):

    name = models.CharField(max_length=100)
    state = models.ForeignKey(State,on_delete=models.CASCADE)

class Student(models.Model):

    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)

    gender=models.CharField(max_length=10)
    dob=models.DateField()

    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15)

    country=models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)
    state=models.ForeignKey(State,on_delete=models.SET_NULL,null=True)
    city=models.ForeignKey(City,on_delete=models.SET_NULL,null=True)

    hobbies=models.CharField(max_length=200)

    avatar = models.ImageField(upload_to="avatars/",null=True,blank=True)
    password=models.CharField(max_length=200,null=True,blank=True)


class Course(models.Model):

    course_name=models.CharField(max_length=200)
    duration=models.CharField(max_length=100)
    fee=models.IntegerField()


class Contact(models.Model):

    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.TextField()