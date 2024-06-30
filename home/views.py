from xmlrpc.client import DateTime
from MySQLdb import Date
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import *
from .form import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

from sklearn.feature_extraction.text import TfidfVectorizer

from joblib import load

model = load("./savemodels/model.joblib")

# from django.contrib.auth import login,authenticate
# Create your views here.

# def index(request):
#     request.session["usertype"] = "null"

#     #return HttpResponse("this is home page")
#     return render(request,"index.html")


def about(request):
    return HttpResponse("this is about page")


def service(request):
    return HttpResponse("this is sevices page")


def contact(request):
    return HttpResponse("this is contact page")


def create(request):
    return render(request, "signup/user_signup.html")


def reporter_signupview(request):
    return render(request, "signup/repoter_signup.html")


num = 0
usertype = ""


def loginView(request):
    # data1=login.objects.all()
    # data1.delete()
    b = user_database.objects.all().values()
    global usertype
    global num
    if request.method == "POST":
        email = request.POST.get("name")
        password = request.POST.get("password")
        i = 0
        j = 0
        for i in range(len(b)):
            if b[i]["email"] == email and b[i]["password"] == password:
                #   user=login(email=email, password=password)
                #   user.save()
                num = 1

                request.session["usertype"] = b[i]["usertype"]
                request.session["username"] = b[i]["username"]

                usertype = b[i]["usertype"]
                request.session["email"] = email
                request.session["password"] = password
                print(request.session["email"])
                print(request.session["password"])

                i = i + 1
                return redirect("home")

    return render(request, "login.html")


def user_signupview(request):
    print("dhqwhdq")
    print(request.method)
    if request.method == "POST":
        firstname = request.POST.get("firstName")
        middlename = request.POST.get("midelname")
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        address = request.POST.get("address", "default")
        school = request.POST.get("school", "default")
        college = request.POST.get("college", "default")
        usertype = request.POST.get("usertype", "user")

        data = user_database(
            firstname=firstname,
            middlename=middlename,
            lastname=lastname,
            email=email,
            phone=phone,
            password=password,
            address=address,
            school=school,
            usertype=usertype,
            username=username,
            college=college,
        )
        data.save()
        print("brt")
        return redirect("login")

    else:
        print("helloo")

    return render(request, "signup/user_signup.html")


def upload(request):
    if request.method == "POST":
        heading = request.POST.get("heading")
        news = request.POST.get("news")
        created_date = request.POST.get("created_date", default=Date.today())
        modify_date = request.POST.get("modify_date", default=Date.today())
        status = request.POST.get("status", default="1")
        news_type = news_type_predictor(news)
        print(news_type_predictor(news)[0])
        data = upload_news(
            heading=heading,
            content=news,
            created_date=created_date,
            modify_date=modify_date,
            status=status,
            username=request.session["username"],
            news_type=news_type,
        )
        data.save()

        mydata = upload_news.objects.all().values()
        print("dddddd")
        print(type(mydata))

        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            fn = form.cleaned_data["image"]

            image1 = reporter_img(
                news_id=mydata[len(mydata) - 1]["news_id"],
                username=request.session["username"],
                image=fn,
            )
            image1.save()

            # form.save()
            obj = form.instance
            print("helllo")
            form = ImageForm()
            img = upload_news.objects.all()
            return redirect("index")
            # return render(request, "index.html", {"data": mydata[::-1], "email": request.session["email"], "password": request.session["password"], "type_of_user": request.session["usertype"], "img": img, "form": form, "username": request.session["username"]})
        form1 = reporter_img.objects.all()
        img = upload_news.objects.all()

    else:
        form = ImageForm()
        print(form)
        form1 = reporter_img.objects.all()
        img = upload_news.objects.all()
        print("harsh")

    # return render(request, "upload_news.html", {"img":img, "form1":form1 ,"form":form })
    return render(
        request,
        "upload_news.html",
        {
            "email": request.session["email"],
            "password": request.session["password"],
            "type_of_user": request.session["usertype"],
            "img": img,
            "form": form,
            "form1": form1,
            "username": request.session["username"],
        },
    )


def index(request):
    mydata = upload_news.objects.all().values()

    data = upload_news.objects.all()
    ad = advertisement.objects.all()
    data2 = reporter_img.objects.all()
    form = ImageForm()
    img = upload_news.objects.all()
    b = []
    a = []
    z = []
    for x in data:
        if x.status == "0":
            b.append(x)

    print("fwtrrttrtr")
    for x in b:
        if x.status == "0":
            big_news = x

    small_news = b[len(b) - 2 : len(b) - 5 : -1]
    rem_news = b[len(b) - 5 : len(b) - 8 : -1]

    if num == 1:
        # email=data1[0]["email"]
        # password=data1[0]["password"]

        return render(
            request,
            "index.html",
            {
                "data": data[::-1],
                "big_news": big_news,
                "rem_news": rem_news,
                "small_news": small_news,
                "data2": data2,
                "email": request.session["email"],
                "password": request.session["password"],
                "type_of_user": request.session["usertype"],
                "img": img,
                "form": form,
                "username": request.session["username"],
                "ad": ad,
            },
        )
    else:
        request.session["usertype"] = "null"
        return render(
            request,
            "index.html",
            {
                "z": z,
                "data": data[::-1],
                "big_news": big_news,
                "small_news": small_news,
                "rem_news": rem_news,
                "img": img,
                "form": form,
                "data2": data2[::-1],
                "ad": ad,
                "a": len(b),
            },
        )


def my_news(request):
    print(request.session["usertype"])

    print(request.session["username"])
    data = upload_news.objects.all().values()
    data2 = reporter_img.objects.all()

    form = ImageForm()
    img = upload_news.objects.all()
    print(num)
    if num == 1:
        # email=data1[0]["email"]
        # password=data1[0]["password"]
        print(data)
        admin = "harsh"

        return render(
            request,
            "my_news.html",
            {
                "data": data[::-1],
                "data2": data2,
                "email": request.session["email"],
                "password": request.session["password"],
                "type_of_user": request.session["usertype"],
                "img": img,
                "form": form,
                "username": request.session["username"],
            },
        )
    else:
        return render(
            request,
            "my_news.html",
            {
                "data": data[::-1],
                "img": img,
                "form": form,
            },
        )


def logoutView(request):
    # request.session["email"]="null"
    # print(request.session.get('name'))
    # return redirect('home')
    global num
    num = 0
    print(num)
    request.session["email"] = "null"
    request.session["usertype"] = "null"
    return redirect("home")


def different_news_page(request):
    data = upload_news.objects.all()
    data2 = reporter_img.objects.all()
    form = ImageForm()
    img = upload_news.objects.all()
    ad = advertisement.objects.all()

    if request.method == "POST":
        type = request.POST.get("type")
        print(type)
        b = []
        for x in data:
            if x.status == "0":
                if x.news_type == type:
                    b.append(x)
                    big_news = x
        print(b)

        small_news = b[len(b) - 2 : len(b) - 5 : -1]
        rem_news = b[len(b) - 5 : len(b) - 8 : -1]
        print(small_news)
        print(rem_news)
    if num == 1:
        return render(
            request,
            "different_news_page.html",
            {
                "type": type,
                "big_news": big_news,
                "data": data[::-1],
                "data2": data2,
                "small_news": small_news,
                "rem_news": rem_news,
                "email": request.session["email"],
                "password": request.session["password"],
                "type_of_user": request.session["usertype"],
                "img": img,
                "form": form,
                "username": request.session["username"],
                "ad": ad,
            },
        )
    else:
        return render(request, "login.html")


def my_admin(request):
    type_of_user = usertype
    data = upload_news.objects.all()
    data2 = reporter_img.objects.all()

    form = ImageForm()
    img = upload_news.objects.all()

    if request.method == "POST":
        condition = request.POST.get("condition")
        key = request.POST.get("primary_key")

        if condition == "approve":
            t = upload_news.objects.all().get(news_id=key)
            t.status = 0
            t.save()
            print(t.status)
        else:
            t = upload_news.objects.all().get(news_id=key)
            t.status = 2
            t.save()
            print(t.status)
        if num == 1:
            # email=data1[0]["email"]
            # password=data1[0]["password"]

            return render(
                request,
                "my_admin.html",
                {
                    "data": data,
                    "data2": data2,
                    "email": request.session["email"],
                    "password": request.session["password"],
                    "type_of_user": request.session["usertype"],
                    "img": img,
                    "form": form,
                    "username": request.session["username"],
                },
            )
    else:
        return render(
            request,
            "my_admin.html",
            {
                "data": data,
                "data2": data2,
                "email": request.session["email"],
                "password": request.session["password"],
                "type_of_user": request.session["usertype"],
                "img": img,
                "form": form,
                "username": request.session["username"],
            },
        )


def detail_news(request):
    if request.method == "POST":
        heading = request.POST.get("heading")
        content = request.POST.get("content")
        news_id = request.POST.get("news_id")
        a = int(news_id)
        print(news_id)
        print(heading)
        data2 = reporter_img.objects.all()

    if request.session["usertype"] == "null":
        print("nll")
        return render(request, "login.html")
    else:
        print("rvetbgv")
        return render(
            request,
            "detail_news.html",
            {
                "heading": heading,
                "content": content,
                "news_id": int(news_id),
                "data2": data2,
                "email": request.session["email"],
                "password": request.session["password"],
                "type_of_user": request.session["usertype"],
                "username": request.session["username"],
            },
        )


def Advertisement(request):
    form = ImageForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        company_name = request.POST.get("company_name")
        name = request.POST.get("name")
        created_date = request.POST.get("created_date", default=Date.today())
        modify_date = request.POST.get("modify_date", default=Date.today())
        fn = form.cleaned_data["image"]

        ad = advertisement(
            company_name=company_name,
            username=name,
            image=fn,
            created_date=created_date,
            modify_date=modify_date,
        )
        ad.save()
        return redirect("index")
    form = AdvertisementForm()
    ad = advertisement.objects.all()
    return render(request, "advertisement.html", {"form": form, "ad": ad})





def news_type_predictor(news):
    # if request.method == "GET":
    #     news = request.GET["news"]

        df = pd.read_csv(r"F:\projects\news-application\result.csv")
        x = df["headline"]
        y = df["category"]
        t = TfidfVectorizer(stop_words="english")
        x_tidf = t.fit_transform(x)

        xtrain, xtest, ytrain, ytest = train_test_split(
            x_tidf, y, test_size=0.20, random_state=42
        )

        model = MultinomialNB()
        model.fit(xtrain, ytrain)
        text = t.transform([news])

        y_pred = model.predict(text)
        return y_pred

    #     return render(request, "result.html", {"result": y_pred})
    # return render(request, "result.html")


def pridictor(request):
    return render(request, "dummy.html")
