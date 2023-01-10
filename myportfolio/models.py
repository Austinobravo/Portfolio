from django.db import models

# Create your models here.

#AboutME 
class About_me(models.Model):
    name = models.CharField(max_length=30, verbose_name='My Name:', help_text='This is the name to appear in the frontend')
    phone = models.IntegerField(verbose_name='My phone number:', help_text='My contact phone number')
    email = models.EmailField(verbose_name='My Email:', help_text='My contact email')
    description = models.TextField(verbose_name='A brief description:', help_text='A little details about me')
    image = models.ImageField(verbose_name='Image:', help_text='An image of me')

    class Meta:
        verbose_name= 'Introduction - About me'
        verbose_name_plural= 'Introduction - About me'

    def __str__(self):
        return self.name


class Projects(models.Model):
    image = models.ImageField(verbose_name='My Project Image:', help_text='The image of each project')
    title = models.CharField(max_length=255, verbose_name='My Project title:', help_text='Title of each project')
    link = models.URLField(verbose_name='Urls Link:', help_text='Links to urls')

    class Meta:
        verbose_name='My Project'
        verbose_name_plural='My Projects'

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name of Sender:', help_text='Name of the sender sending an email')
    email = models.EmailField(verbose_name='Email of Sender:', help_text='Contact email of the sender')
    message = models.TextField(verbose_name='Content Message:', help_text='Message received')

    class Meta:
        verbose_name='My Contact Message'
        verbose_name_plural='My Contact Messages'

    def __str__(self):
        return self.name