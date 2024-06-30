from django.contrib import admin

from home.models import upload_news
from home.models import reporter_img
from home.models import user_database
from home.models import advertisement

# Register your models here.

admin.site.register(user_database)
admin.site.register(upload_news)
admin.site.register(reporter_img)
admin.site.register(advertisement)
