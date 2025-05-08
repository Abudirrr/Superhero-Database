from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Hero, Hire, Category
from .forms import HireForm


# ✅ Home page - list of available heroes
def home(request):
    heroes = Hero.objects.filter(available=True)
    return render(request, "index.html", {"heroes": heroes})


# ✅ Hero detail view
def hero_detail(request, hero_id):
    hero = get_object_or_404(Hero, id=hero_id)
    return render(request, "hero_detail.html", {"hero": hero})


# ✅ Hire page with search and filtering
def hire_page(request):
    query = request.GET.get("q", "")
    category_id = request.GET.get("category")

    heroes = Hero.objects.filter(available=True)
    if query:
        heroes = heroes.filter(name__icontains=query)
    if category_id:
        heroes = heroes.filter(category__id=category_id)

    categories = Category.objects.all()
    context = {
        "heroes": heroes,
        "categories": categories,
        "query": query,
        "category_id": category_id,
    }
    return render(request, "hire.html", context)


# ✅ Hire form - only accessible if logged in
@login_required
def hire_hero(request, hero_id):
    hero = get_object_or_404(Hero, id=hero_id)
    if request.method == "POST":
        form = HireForm(request.POST)
        if form.is_valid():
            hire = form.save(commit=False)
            hire.client = request.user
            hire.hero = hero
            hire.save()
            messages.success(request, "Hero hired successfully!")
            return redirect("dashboard")
    else:
        form = HireForm()

    return render(request, "hire_form.html", {"form": form, "hero": hero})
