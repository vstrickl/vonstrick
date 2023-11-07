from django.shortcuts import render
from django.conf import settings

from .models import PageStyle, NavMenu, SocialMediaItem, Summary, Experience, Achievement, SkillGroup

# Create your views here.
def resume(request):

    title = 'Vonique Stricklen'

    theme = PageStyle.objects.get(pk=1)
    summary = Summary.objects.get(pk=1)
    nav = NavMenu.objects.all()
    social = SocialMediaItem.objects.all()
    experience = Experience.objects.all()
    achievement = Achievement.objects.all()
    skills = SkillGroup.objects.all()

    google_tag_url = settings.MEASUREMENT_ID
    measurement_id = settings.GOOGLE_TAG_URL

    context = {
        'f':theme, 
        'nav':nav,
        's':summary,
        'title':title,
        'skills':skills,
        'social':social, 
        'experience':experience,
        'achievement':achievement,
        'google_tag_url':google_tag_url,
        'measurement_id':measurement_id, 
        }
    
    return render(request, 'resume.html', context)