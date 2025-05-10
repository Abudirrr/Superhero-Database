from django.http import HttpResponse
from django.core.management import call_command
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET

@csrf_exempt
@require_GET
def force_migrations(request):
    try:
        call_command('makemigrations', 'main', interactive=False)
        call_command('migrate', interactive=False)
        return HttpResponse("✅ Migrations forced and applied.")
    except Exception as e:
        return HttpResponse(f"❌ Error during migration: {e}", status=500)
