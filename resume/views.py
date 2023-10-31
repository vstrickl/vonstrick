from django.shortcuts import render

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

    context = {
        'f':theme, 
        'nav':nav,
        'title':title,
        's':summary,
        'social':social, 
        'experience':experience,
        'achievement':achievement,
        'skills':skills,
        }
    
    return render(request, 'resume.html', context)