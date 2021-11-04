from django.contrib import admin

# Register your models here.
from .models import Founditems,ClaimPerson
admin.site.site_header='Welcome to Lost and Found Admin Page'


class Admin(admin.ModelAdmin):
    list_filter = ('date',)
admin.site.register(Founditems)
admin.site.register(ClaimPerson)