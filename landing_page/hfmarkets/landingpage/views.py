# landingpage/views.py

from django.shortcuts import render,redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import TblUsers
from django.contrib.auth.hashers import make_password

def register(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName').strip()
        lastName = request.POST.get('lastName').strip()
        email = request.POST.get('email').strip()
        country = request.POST.get('country').strip()
        country_code = request.POST.get('country_code').strip()
        phone = request.POST.get('phone').strip()
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()

        # Server-side validation
        errors = []  # Collect errors
        if not firstName.isalpha():
            errors.append("First name should only contain letters.")
        if not lastName.isalpha():
            errors.append("Last name should only contain letters.")
        try:
            validate_email(email)
        except ValidationError:
            errors.append("Invalid email format.")
        if not country:
            errors.append("Country must be selected.")
        if not any(char.isdigit() for char in country_code):
            errors.append("Country code must contain at least one number.")
        if not phone.isdigit():
            errors.append("Phone number must contain only numbers.")
        
        if not username:
            errors.append("Username is required.")
        elif TblUsers.objects.filter(username=username).exists():
            errors.append("Username is already taken.")    

        if len(password) < 8:
            errors.append("Password must be at least 8 characters long.")    
        
        if errors:
            # If there are errors, return to the form page with error messages.
            # Assuming you have a context processor for handling messages:
            for error in errors:
                messages.error(request, error)
            return redirect('home')  # Adjust the redirect as needed

        # If validation passes, proceed to create the user
        TblUsers.objects.create(
            firstName=firstName,
            lastName=lastName,
            email=email,
            country=country,
            country_code=country_code,
            phone=phone,
            username=username,
            password=make_password(password)
        )
        return redirect('registration_success')
    else:
        return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')

def registration_success(request):
    return render(request, 'registration_success.html')
