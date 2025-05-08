from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from ..forms import RegistrationForm
from ..models import UserProfile, Hero, Category


# ✅ Register a new user (manual role assignment, Hero auto-create)
def register_user(request):
    """
    Registers a new user and directly creates their UserProfile with the chosen role.
    Also creates a Hero object if role is 'hero'.
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            # 🔒 Check for duplicates
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken.")
                return render(request, 'register.html', {'form': form})

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered.")
                return render(request, 'register.html', {'form': form})

            # ✅ Create User and Profile
            user = User.objects.create_user(username=username, email=email, password=password)
            UserProfile.objects.create(user=user, role=role)

            # 🦸 Create Hero if applicable
            if role == 'hero':
                default_category = Category.objects.first()
                if not default_category:
                    messages.error(request, "No category available. Please ask admin to add one.")
                    return render(request, 'register.html', {'form': form})

                Hero.objects.create(
                    user=user,
                    name=username,
                    description="This hero has no description yet.",
                    category=default_category,
                    available=True,
                    power_level=1,
                    price=100.00,
                )

            messages.success(request, "Account created. Please log in.")
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


# ✅ Login with role-based redirection
def login_user(request):
    """
    Authenticates user and redirects them based on their assigned role.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            if user.is_superuser:
                return redirect('/admin/')

            try:
                role = user.userprofile.role
            except UserProfile.DoesNotExist:
                logout(request)
                messages.error(request, "User profile missing. Please contact support.")
                return redirect('login')

            if role == 'client':
                return redirect('client_dashboard')
            elif role == 'hero':
                return redirect('hero_dashboard')
            elif role == 'support':
                return redirect('support_dashboard')
            else:
                return HttpResponseForbidden("Invalid role.")

        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')


# ✅ Logout
@login_required
def logout_user(request):
    """
    Logs the user out and redirects to the login page.
    """
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')
