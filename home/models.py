from django.db import models

# Create your models here.


  
    
class login(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.type
    
class user_data(models.Model):
    firstname = models.CharField(max_length=50)
    midlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50,default="patidarr")
    gender = models.CharField(max_length=50)
    birth= models.DateField(max_length=50,default="1111/11/11")
    email = models.CharField(max_length=50,default="harsh@gmail.com")
    phone = models.CharField(max_length=10,default="1111111111")
    password = models.CharField(max_length=50,default="harsh")
    def __str__(self):
        return self.email
    
class upload(models.Model):
    image=models.ImageField(upload_to='img/%y')
    caption=models.CharField(max_length=50)
    news=models.CharField(max_length=10000)
    def __str__(self):
        return self.caption
    
  
    def __str__(self):  
        return self.caption  
    
class reporter(models.Model):
    firstname = models.CharField(max_length=50)
    midlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50,default="patidarr")
    gender = models.CharField(max_length=50)
    birth= models.DateField(max_length=50,default="1111/11/11")
    email = models.CharField(max_length=50,default="harsh@gmail.com")
    phone = models.CharField(max_length=10,default="1111111111")
    password = models.CharField(max_length=50,default="harsh")
    adress = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    college = models.CharField(max_length=50)
    skill = models.CharField(max_length=50)
    
    def __str__(self):
        return self.firstname
    
class user_database(models.Model):
    firstname = models.CharField(max_length=50)
    midlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=8)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=10, default="0000000000")
    adress = models.CharField(max_length=50, default="no")
    school = models.CharField(max_length=50, default="no")
    collage = models.CharField(max_length=60, default="no")
    qualification = models.ImageField(upload_to='img/%y')
    image = models.ImageField(upload_to='img/%y')
    usertype = models.CharField(max_length=50, default="user")
