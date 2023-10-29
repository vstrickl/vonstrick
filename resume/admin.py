from django.contrib import admin

from .models import FontFamily, PageStyle, NavMenu, Summary, SocialMediaItem, Achievement, Experience, Company, Skill, SkillGroup

# Register your models here.
admin.site.register(Summary)
admin.site.register(SocialMediaItem)

class CompanyAdmin(admin.ModelAdmin):

    search_fields = ['name']

admin.site.register(Company, CompanyAdmin)

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

class ExperienceAdmin(admin.ModelAdmin):

    autocomplete_fields = ['company','achievements']
    list_display = ("time_frame", "display_companies", "job_title")

    def display_companies(self, obj):
        return ", ".join([company.name for company in obj.company.all()])

admin.site.register(Experience, ExperienceAdmin)

class AchievementAdmin(admin.ModelAdmin):

    autocomplete_fields = ['company']
    search_fields = ['date','company']
    list_display = ("date", "display_companies")

    def display_companies(self, obj):
        return ", ".join([company.name for company in obj.company.all()])

admin.site.register(Achievement, AchievementAdmin)

class SkillAdmin(admin.ModelAdmin):

    search_fields = ['type']

admin.site.register(Skill, SkillAdmin)

class SkillGroupAdmin(admin.ModelAdmin):

    autocomplete_fields = ['skills']

admin.site.register(SkillGroup, SkillGroupAdmin)