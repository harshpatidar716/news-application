from xmlrpc.client import DateTime
from MySQLdb import Date
from django.db import models

# Create your models here.


class reporter_img(models.Model):
    news_id = models.IntegerField(max_length=50)
    image = models.FileField(upload_to="img/%y")
    username = models.CharField(max_length=50, default="username")

    def __str__(self):
        return self.username


class advertisement(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.FileField(upload_to="img/%y")
    username = models.CharField(max_length=50, default="username")
    company_name = models.CharField(max_length=50, default="username")
    created_date = models.DateField(default=Date.today())
    modify_date = models.DateField(default=Date.today())


class upload_news(models.Model):
    news_id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=50)
    content = models.CharField(max_length=10000)
    created_date = models.DateField(default=Date.today())
    modify_date = models.DateField(default=Date.today())
    status = models.CharField(max_length=50, default="1")
    username = models.CharField(max_length=50, default="username")
    news_type = models.CharField(max_length=50, default="news")

    def __str__(self):
        return self.heading


class user_database(models.Model):
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=8)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=10, default="0000000000")
    image = models.ImageField(upload_to="img/%y")
    usertype = models.CharField(max_length=50, default="user")

    def __str__(self):
        return self.email
