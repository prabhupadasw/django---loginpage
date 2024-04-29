from django.shortcuts import render,redirect
from .forms import CreateUserForm,Loginform
#-authentication models and function
from django .contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout
def homepage(request):

    return render(request,"index.html")

def register(request):

    form = CreateUserForm()

    if request.method=="POST":

        form =  CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("mylogin")
        
    context = {'registerform':form}

    return render(request,'register.html',context=context)
    
def mylogin(request):
    form = Loginform()
    if request.method == "POST":
        form = Loginform(data=request.POST)
        if form.is_valid():  # corrected method name from `ia_valid` to `is_valid`
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")

    context = {'loginform': form}  # corrected dictionary declaration
    return render(request, "mylogin.html", context=context)
def dashboard(request):
    return render(request,"dashboard.html")
def user_logout(request):
    auth.logout(request)
    return redirect("")
 
