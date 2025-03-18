from django.shortcuts import render, redirect, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Property, Appointment
from .forms import PropertyForm,  AppointmentForm

# Admin Login
def admin_login(request):
    if request.user.is_authenticated:
        return redirect('admin_dashboard')

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('admin_dashboard')
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})

# Admin Dashboard
@login_required
def admin_dashboard(request):
    properties = Property.objects.all()
    appointments = Appointment.objects.all()
    return render(request, "admin_dashboard.html", {"properties": properties, "appointments": appointments})

# Logout
def admin_logout(request):
    logout(request)
    return redirect('admin_login')


def home(request):
    properties = Property.objects.all()  # Fetch all properties
    return render(request, 'home.html', {'properties': properties})










@login_required
def add_property(request):
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')  # Redirect after saving
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})

@login_required
def edit_property(request, id):
    property_obj = get_object_or_404(Property, id=id)
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES, instance=property_obj)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = PropertyForm(instance=property_obj)
    return render(request, 'edit_property.html', {'form': form})

@login_required
def delete_property(request, id):
    property_obj = get_object_or_404(Property, id=id)
    property_obj.delete()
    return redirect('admin_dashboard')


@login_required
def admin_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'admin_appointments.html', {'appointments': appointments})






def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')  # Redirect to success page
    else:
        form = AppointmentForm()

    return render(request, 'book_appointment.html', {'form': form})

def appointment_success(request):
    return render(request, 'appointment_success.html')


