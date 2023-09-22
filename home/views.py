from xmlrpc.client import DateTime
from MySQLdb import Date
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import upload_news,user_database,report_image
from .form import ImageForm

# from django.contrib.auth import login,authenticate
# Create your views here.

def index(request):
   
    #return HttpResponse("this is home page")
    return render(request,"index.html")

def about(request):
    return HttpResponse("this is about page")

def service(request):
    return HttpResponse("this is sevices page")

def contact(request):
    return HttpResponse("this is contact page")

def create(request):
     return render(request,"signup/user_signup.html")
 
def reporter_signupview(request):
       return render(request, "signup/repoter_signup.html")
   

num=0
usertype="user"
def loginView(request):
    b=user_database.objects.all().values()
    global usertype
    global num
    if request.method == "POST":
        email = request.POST.get('name')
        password = request.POST.get('password')
        i=0
        j=0
        for i in range(len(b)):
            
            if(b[i]['email']==email and b[i]['password']==password):
            #   user=login(email=email, password=password)
            #   user.save()
              num=1
            #   usertype=b[i]["usertype"]
              request.session["usertype"] = b[i]["usertype"]
              request.session["username"] = b[i]["username"]
             
              
              request.session["email"] = email
              request.session["password"] = password
              print(request.session["email"])
              print(request.session["password"])

              i=i+1
              return redirect("home")
            i=i+1
            print(i)
    
    return render(request,"login.html")

def user_signupview(request):
    print("dhqwhdq")
    print(request.method)
    if request.method == "POST":
       
        firstname = request.POST.get('firstName')
        midlename = request.POST.get('midelname')
        lastname = request.POST.get('lastname')
        username=request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        address = request.POST.get('address', "default")
        school = request.POST.get('school', "default")
        collage=request.POST.get('college',"default")
        usertype = request.POST.get('usertype', "user")
      
        data = user_database(firstname = firstname, midlename=midlename, lastname=lastname,  email=email, phone=phone, password=password,adress=address, school=school, usertype=usertype, username=username, collage=collage)
        data.save()
        print("brt")
        return redirect('login')
        
    else:
        print("helloo")
        
    return render(request,"signup/user_signup.html")


def upload(request):
    
    
    if request.method == "POST":
        
        heading = request.POST.get('heading')
        news = request.POST.get('news')
        created_date=request.POST.get("created_date",default=Date.today())
        modify_date=request.POST.get("modify_date",default=Date.today())
        status=request.POST.get("status",default="1")
        
        data=upload_news(heading=heading, content=news, created_date=created_date, modify_date=modify_date, status=status,username=request.session["username"])
        data.save()
        
        print("dddddd")
        form=ImageForm(request.POST,request.FILES)
        
        # image = request.FILES.getlist('images')
        # for image in image:
        #     report_image.objects.create(image=image)
        if form.is_valid():
            form.save()
            obj=form.instance
            print("helllo")
            form=ImageForm()
            img=upload_news.objects.all()
            return redirect("home")
        form = report_image.objects.all()
        img=upload_news.objects.all()
        
    else:
        # form=ImageForm()
        form = report_image.objects.all()
        img=upload_news.objects.all()
        print("harsh")
    return render(request,"upload_news.html",{"img":img,"form":form})

def index(request):
    mydata = upload_news.objects.all().values()
    
    data=upload_news.objects.all()
    data2=report_image.objects.all()
    form=ImageForm()
    img=upload_news.objects.all()
    if(num==1):
        # email=data1[0]["email"]
        # password=data1[0]["password"]
        
        
        return render(request, "index.html",{"data": data , "data2": data2 ,"email":request.session["email"], "password":request.session["password"] ,"type_of_user":request.session["usertype"], "img":img,"form":form})
    else:
        return render(request, "index.html",{"data": data , "img":img,"form":form, "data2": data2} )

def my_news(request):
    
    print(request.session["usertype"])
    
    print(request.session["username"])
    data=upload_news.objects.all()
    data2=report_image.objects.all()
    
    form=ImageForm()
    img=upload_news.objects.all()
    if(num==1):
        # email=data1[0]["email"]
        # password=data1[0]["password"]
        print(data)
        admin="harsh"
        return render(request, "my_news.html",{"data": data , "data2": data2 ,"email":request.session["email"], "password":request.session["password"] ,"type_of_user":request.session["usertype"], "img":img,"form":form, "username":request.session["username"]})
    else:
        return render(request, "my_news.html",{"data": data ,  "img":img,"form":form})


def my_admin(request):

    type_of_user=usertype
    data=upload_news.objects.all()
    data2=report_image.objects.all()
    
    form=ImageForm()
    img=upload_news.objects.all()
    
    if request.method == "POST":
        
        condition = request.POST.get('condition')
        key = request.POST.get('primary_key')
       
        if(condition=="approve"):
            t = upload_news.objects.all().get(primary_key = key)
            t.status=0
            t.save()
            print(t.status)
        else:
            t = upload_news.objects.all().get(primary_key = key)
            t.status=2
            t.save()
            print(t.status)
        if(num==1):
        # email=data1[0]["email"]
        # password=data1[0]["password"]
        
        
            return render(request, "my_admin.html",{"data": data , "data2": data2 ,"email":request.session["email"], "password":request.session["password"] ,"type_of_user":request.session["usertype"], "img":img,"form":form})
    else:
        return render(request, "my_admin.html",{"data": data , "data2": data2 ,"email":request.session["email"], "password":request.session["password"] ,"type_of_user":request.session["usertype"], "img":img,"form":form})
    

def logoutView(request):
   
   
    global num
    num=0
    print(num)
    request.session["email"]="null"
    
    return redirect('home')
    

# def logoutView(request):