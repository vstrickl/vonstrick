from django.contrib import admin

from .models import FontFamily, PageStyle, NavMenu, Summary, SocialMenu

# Register your models here.
admin.site.register(Summary)
admin.site.register(SocialMenu)

class FontFamilyAdmin(admin.ModelAdmin):

    list_display = ("family_name", "serif_type")
    search_fields = ['family_name']

admin.site.register(FontFamily, FontFamilyAdmin)

class PageStyleAdmin(admin.ModelAdmin):

    autocomplete_fields = ['header_font', 'font']

admin.site.register(PageStyle, PageStyleAdmin)

class NavMenuAdmin(admin.ModelAdmin):
    list_display = ("title", "url")

admin.site.register(NavMenu, NavMenuAdmin)