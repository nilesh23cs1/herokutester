from django.shortcuts import render,redirect             #import redirect here
from .forms import CustomRegistrationform
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':
        registerform=CustomRegistrationform(request.POST)
        if registerform.is_valid():
            registerform.save()
            messages.success(request, ("New User Account Created,Login to get started"))

        return redirect('registername')


    else:
        registerform=CustomRegistrationform()
        return render(request,'register.html',{'registerform':registerform})