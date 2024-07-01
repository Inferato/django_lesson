from django.contrib import admin
from .models import Comments, Posts

admin.site.register(Posts)
admin.site.register(Comments)
