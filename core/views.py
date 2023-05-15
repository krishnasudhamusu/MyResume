from django.shortcuts import render
from . import models
from django.shortcuts import redirect


# Create your views here.


def home(request):
    context = {'home': 'active'}
    return render(request, 'core/home.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        ins = models.Contact(name=name, email=email, subject=subject, message=message)
        ins.save()
        return render(request, 'core/thankyou.html')

    context = {'contact': 'active'}
    return render(request, 'core/contact.html', context)
