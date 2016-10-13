from django.contrib import admin

# Register your models here.

from asset import models
from asset.user_admin import UserAdmin

admin.site.register(models.UserProfile,UserAdmin)

# 取消注册group在后头显示
from django.contrib.auth.models import Group
# admin.site.unregister(Group)