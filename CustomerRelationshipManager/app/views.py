from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Records
# Create your views here.

###### FUNCTION BASED VIEWS ######

def home(request):
    records = Records.objects.all()
    return render(request=request, template_name='home.html', context={'records': records})

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
            messages.success(request=request, message="Log in Failed, Please try again.")
            return redirect('app:Home')
    else:
        return render(request=request, template_name='home.html')
    

def logout_user(request):
    logout(request=request)
    print("logout catch")
    messages.success(request=request, message="Log out successful")
    return redirect('app:Home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(f"form: {form}")
        if form.is_valid():
            print("====>>>>form validated")
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
        # return render(request=request, template_name='register.html', context={'form': form})
    return render(request=request, template_name='register.html', context={'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_rec = Records.objects.get(id=pk)
        return render(request, 'record.html', context={'cust_rec': customer_rec})
    else:
        messages.success(request, "You must be logged in...")
        return redirect('app:Home')
    

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Records.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record deleted successfully.")
        # return redirect('app:Home')
    else:
        messages.success(request, "You must be logged in...")
    return redirect('app:Home')


def add_record(request):
    add_form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if add_form.is_valid():
                add_record = add_form.save()
                messages.success(request, "Record added successfully...")
                return redirect('app:Home')   
        return render(request, 'add_record.html', {'add_form': add_form})
    else:
        messages.success(request, "You must Login to add any record...")
        return redirect('app:Home')



