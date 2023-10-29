from django.shortcuts import render

from .models import NavMenu, SocialMenu

# Create your views here.
def resume(request):

    nav = NavMenu.objects.all()
    social = SocialMenu.objects.all()

    context = {
        'nav':nav,    
        'social':social,  
        }
    
    return render(request, 'resume.html', context)