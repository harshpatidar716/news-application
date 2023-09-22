from django.contrib import admin
# from home.models import login
# from home.models import user_data
# from home.models import reporter,user_database
from home.models import upload_news,user_database, report_image



# Register your models here.
# admin.site.register(login)
# admin.site.register(user_data)
# admin.site.register(reporter)
admin.site.register(upload_news)
admin.site.register(user_database)
admin.site.register(report_image)