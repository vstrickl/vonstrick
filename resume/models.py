from django.db import models

# Create your models here.
class FontFamily(models.Model):
    family_name = models.CharField(max_length=200, null=True, blank=True)
    serif_type = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"'{self.family_name}', {self.serif_type}"
    
class PageStyle(models.Model):
    template_name = models.CharField(max_length=200,null=True, blank=True)
    header_font = models.ManyToManyField(FontFamily, blank=True, related_name='headers')  
    header_font_size = models.CharField(max_length=200, null=True, blank=True)
    header_font_weight = models.CharField(max_length=200, null=True, blank=True)
    font = models.ManyToManyField(FontFamily, blank=True, related_name='general')  
    font_size = models.CharField(max_length=200, null=True, blank=True)
    font_weight = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.template_name
    
class NavMenu(models.Model):
    title = models.CharField(max_length=200,null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
    
class Summary(models.Model):
    intro = models.CharField(max_length=200,null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    objective = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.intro
    
class SocialMenu(models.Model):
    social = models.CharField(max_length=200, null=True, blank=True)
    font_awesome = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.social