from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from main.models import Hero, Rating

# ===============================
# AJAX Hero Rating View
# ===============================
@csrf_exempt  # Optional: only use if your JS doesn't send CSRF tokens
@require_POST
@login_required
def rate_hero(request):
    """
    Allows logged-in users to rate a hero from 1 to 5 stars.
    Handles AJAX POST requests and returns a JSON response.
    """
    try:
        hero_id = int(request.POST.get('hero_id'))
        stars = int(request.POST.get('stars'))

        if not (1 <= stars <= 5):
            return JsonResponse({'success': False, 'error': 'Invalid rating value.'})

        hero = get_object_or_404(Hero, id=hero_id)

        Rating.objects.update_or_create(
            user=request.user,
            hero=hero,
            defaults={'stars': stars}
        )

        return JsonResponse({'success': True})

    except (TypeError, ValueError):
        return JsonResponse({'success': False, 'error': 'Invalid input.'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
