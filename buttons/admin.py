from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Button, ButtonCategory, Tags, Qualities

# Register your models here.
admin.site.register(Button)
admin.site.register(ButtonCategory)
admin.site.register(Tags)
admin.site.register(Qualities)