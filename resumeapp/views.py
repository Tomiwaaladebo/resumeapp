from django.core.checks import messages
from django.shortcuts import redirect, render
from resumeapp.models import Contact
from django.contrib import messages
from django.http import HttpResponse

#from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.template import RequestContext
from django.core.mail import send_mail

def index(request):
    
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            Contact.objects.create(
                name = name,
                email = email,
                subject = subject,
                message = message
            ).save()
            
            messages.success(request, name)
            return redirect('success')
        except:
            return HttpResponse('invalid entry, Try again')
    return render(request, 'resumeapp/index.html')

def success(request):
    
    
    return render(request, 'resumeapp/success.html')
