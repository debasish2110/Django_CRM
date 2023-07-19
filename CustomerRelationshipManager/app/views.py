from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

###### FUNCTION BASED VIEWS ######

def home(request):
    # check login
    if request.method == 'POST':
        # fetching the username from post
        # user_nameand password key is same as the name defined in the form input tag.
        # home.html line no 15 and 18
        username = request.POST['user_name']
        password = request.POST['password']

        #authenticating the user.
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

# def login_user(request):
#     pass

def logout_user(request):
    logout(request=request)
    messages.success(request=request, message="Log out successful")
    return redirect('app:Home')

