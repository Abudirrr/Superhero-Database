from django.http import HttpResponse
from django.core.management import call_command
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def trigger_migrations(request):
    call_command('migrate', interactive=False)
    return HttpResponse("✅ Migrations applied.")
