from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse
# Create your views here.

def index(request):
    #About me Section
    about_me = About_me.objects.all()

    #Projects Section
    projects = Projects.objects.all()

    #Contact me Section
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = f'Message from: {form.cleaned_data["name"]} and Email: {form.cleaned_data["email"]}'
            email_message = form.cleaned_data['message']
            CONTACT_EMAIL = 'austinobravo@gmail.com'
            ADMIN_EMAIL = ['support1@elitenessee.com', 'austinobravo@gmail.com']
            try:
                send_mail(name, email_message, CONTACT_EMAIL, ADMIN_EMAIL, fail_silently=True)
            except BadHeaderError:
                return HttpResponse('An error occurred, Fill form again.')


            form.save()
            messages.success(request, 'Your Application have been submitted')

        else:
            messages.error(request, 'Your email is invalid')
            form = ContactForm()


        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # message = request.POST.get('message')

        #Fixing the message in a model
        # contact = Contact(
        #     name=name,
        #     email=email,
        #     message=message
        # )
        # contact.save()
        
    form = ContactForm()

    context = {
        'me': about_me,
        'project': projects,
        'form': form
    }

    return render(request, 'index.html', context)
