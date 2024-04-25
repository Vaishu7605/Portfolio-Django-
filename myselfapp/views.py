from django.shortcuts import render,redirect
from .models import message
from .form import *



def index(request):
    if request.method == 'POST':
        Your_Name=request.POST.get('name')
        Your_Email=request.POST.get('email')
        Subject=request.POST.get('subject')
        Message=request.POST.get('message')

        a=message.objects.create(
            Your_Name=Your_Name,
            Your_Email=Your_Email,
            Subject=Subject,
            Message=Message
            )
        a.save()
        return redirect('index')
    return render(request,'index.html')
           



# Create your views here.
