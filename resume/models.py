from django.db import models

# Create your models here.
class NavMenu(models.Model):
    title = models.CharField(max_length=200,null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
    
class SocialMenu(models.Model):
    social = models.CharField(max_length=200, null=True, blank=True)
    font_awesome = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.social
