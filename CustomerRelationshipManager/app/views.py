from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.

###### FUNCTION BASED VIEWS ######

def home(request):
    return render(request=request, template_name='home.html')

def login_user(request):
    # check login
    if request.method == 'POST':
        # fetching the username from post
        # username and password key is same as the name defined in the form input tag.
        # home.html line no 15 and 18
        username = request.POST['username']
        password = request.POST['password']

        # authenticating the user.
        user = authenticate(request=request, username=username, password=password)

        # need to define meesages in base.html
        if user is not None:
            # if user is authenticated then logging in the user
            login(request=request, user=user)
            messages.success(request=request, message="Log in successful")
            # redirecting to the target view.
            return redirect('app:Home')
        else:
            messages.MessageFailure(request=request, message="Log in Failed, Please try again.")
            return redirect('app:Home')
    else:
        return render(request=request, template_name='home.html')
    

def logout_user(request):
    logout(request=request)
    messages.success(request=request, message="Log out successful")
    return redirect('app:Home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:Home')
            # authenticate and login...
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']

            # user = authenticate(request=request, username=username, password=password)
            # login(request=request, user=user)
            # messages.success(request=request, message="Log in successful")
            # return redirect('app:Home')           
    else:
        form = SignUpForm()
        return render(request=request, template_name='register.html', context={'form': form})

