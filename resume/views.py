from django.shortcuts import render

from .models import NavMenu, Summary, SocialMenu, PageStyle

# Create your views here.
def resume(request):

    nav = NavMenu.objects.all()
    summary = Summary.objects.get(pk=1)
    social = SocialMenu.objects.all()
    theme = PageStyle.objects.get(pk=1)

    context = {
        'nav':nav,
        's':summary,
        'social':social, 
        'f':theme, 
        }
    
    return render(request, 'resume.html', context)