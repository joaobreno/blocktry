from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Mail

def direct_message(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        comments = request.POST['comments']
        mail = Mail.objects.create(name=name, email=email, phone=phone,message=comments)
        mail.save()
        messages.success(request, 'Message sent successfully')
        return redirect('contact')
    else:
        return redirect('contracts/contact')
