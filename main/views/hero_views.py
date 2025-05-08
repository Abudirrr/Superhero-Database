from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta

from ..models import Hero, Category, Hire
from ..forms import HireForm

# ✅ Home Page
def home(request):
    heroes = Hero.objects.filter(available=True)
    return render(request, 'index.html', {'heroes': heroes})

# ✅ Hero Details
def hero_detail(request, hero_id):
    hero = get_object_or_404(Hero, id=hero_id)
    return render(request, 'hero_detail.html', {'hero': hero})

# ✅ Recommended Heroes (Same Category)
def recommended_heroes(request, hero_id):
    current_hero = get_object_or_404(Hero, id=hero_id)
    recommendations = Hero.objects.filter(category=current_hero.category).exclude(id=hero_id)[:4]
    return render(request, 'recommendations.html', {'recommendations': recommendations})

# ✅ Hire Listing with Filters
def hire_page(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    power_level = request.GET.get('power_level')

    heroes = Hero.objects.filter(available=True)

    if query:
        heroes = heroes.filter(name__icontains=query)
    if category_id:
        heroes = heroes.filter(category__id=category_id)
    if min_price:
        heroes = heroes.filter(price__gte=min_price)
    if max_price:
        heroes = heroes.filter(price__lte=max_price)
    if power_level:
        heroes = heroes.filter(power_level__gte=power_level)

    categories = Category.objects.all()
    context = {
        'page_obj': heroes,
        'categories': categories,
        'query': query,
        'category_id': category_id,
        'min_price': min_price,
        'max_price': max_price,
        'power_level': power_level
    }
    return render(request, 'hire.html', context)

# ✅ Hero Hiring with Validations
@login_required
def hire_hero(request, hero_id):
    hero = get_object_or_404(Hero, id=hero_id)

    if request.method == 'POST':
        form = HireForm(request.POST)
        if form.is_valid():
            mission_name = form.cleaned_data['mission_name']

            # Check if hero is available
            if not hero.available:
                messages.error(request, "This hero is currently unavailable.")
                return redirect('hire')

            # Prevent hiring same hero in past 24 hours
            recent_hires = Hire.objects.filter(
                hero=hero,
                date_hired__gte=timezone.now() - timedelta(hours=24)
            )
            if recent_hires.exists():
                messages.warning(request, "This hero has already been hired recently.")
                return redirect('hire')

            # Prevent same user from hiring the same hero more than once
            if Hire.objects.filter(client=request.user, hero=hero).exists():
                messages.warning(request, "You have already hired this hero.")
                return redirect('client_dashboard')

            # Save the hire
            hire = form.save(commit=False)
            hire.client = request.user
            hire.hero = hero
            hire.save()

            messages.success(request, f"You successfully hired {hero.name} for '{mission_name}'!")
            return redirect('client_dashboard')
    else:
        form = HireForm()

    return render(request, 'hire_form.html', {'form': form, 'hero': hero})
