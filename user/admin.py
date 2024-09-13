from django.contrib import admin
from user.models import User
from django.contrib.auth.models import Group
admin.site.unregister(Group)
@admin.register(User)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("username",)
    fields = ("username", "password")