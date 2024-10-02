# from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("<h1>Welcome to Holiday Hotel!</h1><p>This is a simple Django website.</p>")
# from django.shortcuts import render

# def home(request):
#     return render(request, 'myapp/home.html')
from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Reservation

def home(request):
    return render(request, 'myapp/home.html')

def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Process the form and save the reservation to the database
            form.save()
            return redirect('view_reservation')  # Redirect to view reservations after successful submission
    else:
        form = ReservationForm()  # Render an empty form for GET requests
    
    return render(request, 'myapp/create_reservation.html', {'form': form})

# def view_reservation(request):
#     # Fetch and display reservations
#     return render(request, 'myapp/view_reservation.html')

# views.py
from django.shortcuts import render
from .models import Reservation

def view_reservation(request):
    # Query all rows from the Reservation table
    reservations = Reservation.objects.all()
    
    # Pass the reservations to the template
    return render(request, 'myapp/view_reservation.html', {'reservations': reservations})

