from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(LogIn)
admin.site.register(Register)
admin.site.register(Feedback)

