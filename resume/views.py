from django.shortcuts import render

from .models import PageStyle, NavMenu, SocialMediaItem, Summary, Experience

# Create your views here.
def resume(request):

    theme = PageStyle.objects.get(pk=1)
    nav = NavMenu.objects.all()
    social = SocialMediaItem.objects.all()
    summary = Summary.objects.get(pk=1)
    experience = Experience.objects.all()

    context = {
        'f':theme, 
        'nav':nav,
        'social':social, 
        's':summary,
        'experience':experience
        }
    
    return render(request, 'resume.html', context)