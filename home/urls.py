from django.contrib import admin
from django.urls import path, include
from home import views
from .views import index
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="home"),
    path("index/", views.index, name="index"),
    path("about", views.about, name="about"),
    path("service", views.service, name="service"),
    path("contact", views.contact, name="contact"),
    path("login/", views.loginView, name="login"),
    path("logout/", views.logoutView, name="logout"),
    path("user_signup/", views.user_signupview, name="user_signup"),
    path("reporter_signup/", views.reporter_signupview, name="reporter_signup"),
    path("upload_news/", views.upload, name="upload_news"),
    path("my_news/", views.my_news, name="my_news"),
    path("my_admin/", views.my_admin, name="my_admin"),
    path("detail_news/", views.detail_news, name="detail_news"),
    path("different_news_page/", views.different_news_page, name="different_news_page"),
    path("Advertisement/", views.Advertisement, name="Advertisement"),
    # path("result", views.forminfo, name="result"),
    path("dummy", views.pridictor, name="pridictor"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
