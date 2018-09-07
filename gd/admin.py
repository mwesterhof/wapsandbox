from django.contrib import admin

from .models import Hobby, Job, Person


admin.site.register([Hobby, Job, Person])
