from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import Profile
from django.views.generic import TemplateView
from .models import Car 
from .forms import SearchForm




@login_required(login_url='login')
def profile(request):
    if request.user.is_authenticated:
            return redirect('index')
    else:
        if request.method == 'POST':
            form = Profile(request.POST, request.FILES, instance=request.user.profile)
            if form.is_valid():
                form.save()
                return redirect('profile')
        else:
            form = Profile(instance=request.user.profile)

    return render(request, 'profile.html', {'form': form})


def register(request):
    if request.user.is_authenticated:
            return redirect('index')
    else:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)  # Log the user in after registration
                return redirect('home')  # Redirect to the homepage
        else:
            form = CustomUserCreationForm()
    return render(request, 'transpo/user/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('home')  # Replace 'home' with the name of your desired view
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'transpo/user/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')





def index(request):
    return render(request, 'transpo/index.html')


@login_required(login_url='login')
def home(request):
    return render(request, 'transpo/home.html')


@login_required(login_url='login')
def book_vehicle(request):
    if request.method == "POST":
        # Get data from the form
        vehicle_type = request.POST.get('vehicle_type')
        pickup_location = request.POST.get('pickup_location')
        dropoff_location = request.POST.get('dropoff_location')
        date = request.POST.get('date')

        # Here you can add logic to process the booking, like saving it to a database
        return HttpResponse(f"Booking successful! Vehicle: {vehicle_type}, Date: {date}")

    # Render the booking form for GET request
    return render(request, 'transpo/booking/book_vehicle.html')


@login_required(login_url='login')
def car_rental(request):
       cars = Car.objects.all()
       return render(request, 'transpo/rental/car_rental.html', {'cars': cars})



@login_required(login_url='login')
def search_view(request):
    form = SearchForm(request.GET) 
    if form.is_valid():

        model = form.cleaned_data['model']
        brand = form.cleaned_data['brand']
        year = form.cleaned_data['year']
        price_limit = form.cleaned_data['price_limit']
        

        filtered_items = []
    
        return render(request, 'search_results.html', {'form': form, 'filtered_items': filtered_items})
    
    return render(request, 'search_page.html', {'form': form})


