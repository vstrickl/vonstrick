from django.contrib import admin

from .models import NavMenu, SocialMenu

# Register your models here.
admin.site.register(SocialMenu)

class NavMenuAdmin(admin.ModelAdmin):
    list_display = ("title", "url")

admin.site.register(NavMenu, NavMenuAdmin)