from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings 

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()

        # Sending mail
        # send_mail(
        #     f'Hello {name}',
        #     'Your feedback has been successfully recieved and we will be in touch with you shortly.',
        #     'raphaelchris252@gmail.com',
        #     [email],
        #     fail_silently=False
        # )

        messages.success(request,"Your message has been recieved, we will send a response shortly.")
        return redirect('index')

    return render(request,'index.html')