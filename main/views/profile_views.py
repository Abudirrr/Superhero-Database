from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from ..models import Hero, Rating, UserProfile
from ..forms import ProfileForm


@csrf_exempt
@login_required
def rate_hero(request):
    """
    Allows a logged-in user to rate a hero using AJAX POST.
    Expects 'hero_id' and 'stars' in the POST data.
    """
    if request.method == 'POST':
        hero_id = request.POST.get('hero_id')
        stars = request.POST.get('stars')
        if not hero_id or not stars:
            return JsonResponse({'success': False, 'error': 'Missing data'})

        try:
            stars = int(stars)
            hero = get_object_or_404(Hero, id=hero_id)
            Rating.objects.update_or_create(
                user=request.user,
                hero=hero,
                defaults={'stars': stars}
            )
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})


@login_required
def edit_profile(request):
    """
    Allows a logged-in user to view and update their profile.
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('edit_profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'edit_profile.html', {
        'form': form,
        'user_profile': user_profile
    })
