from django.contrib import admin
from .models import Postmodel,Comment
# Register your models here.

class Postmodeladmin(admin.ModelAdmin):
    list_display=('title','date_created')

admin.site.register(Postmodel, Postmodeladmin)
admin.site.register(Comment)