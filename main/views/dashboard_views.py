from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from ..models import Hire, Message, UserProfile, Hero
from ..forms import HeroUpdateForm  # ✅ Ensure this form is defined

@login_required
def dashboard(request):
    """
    Redirects the user to the appropriate dashboard based on their role.
    """
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        return HttpResponseForbidden("User profile missing.")

    if profile.role == 'client':
        return redirect('client_dashboard')
    elif profile.role == 'hero':
        return redirect('hero_dashboard')
    elif profile.role == 'support':
        return redirect('support_dashboard')
    elif profile.role == 'admin':
        return redirect('/admin/')

    return HttpResponseForbidden("Access denied")


@login_required
def client_dashboard(request):
    """
    Dashboard for clients to view their hero hires.
    """
    if request.user.userprofile.role != 'client':
        return HttpResponseForbidden("Access denied.")

    hires = Hire.objects.filter(client=request.user).order_by('-date_hired')
    return render(request, "client_dashboard.html", {"hires": hires})


@login_required
def hero_dashboard(request):
    """
    Dashboard for heroes to view and update their profile including image.
    """
    if request.user.userprofile.role != 'hero':
        return HttpResponseForbidden("Access denied.")

    try:
        hero = Hero.objects.get(user=request.user)
    except Hero.DoesNotExist:
        return HttpResponseForbidden("Hero profile not linked to this user.")

    assignments = Hire.objects.filter(hero=hero).order_by('-date_hired')

    if request.method == 'POST':
        form = HeroUpdateForm(request.POST, request.FILES, instance=hero)
        if form.is_valid():
            form.save()
            messages.success(request, "Hero profile updated successfully.")
            return redirect('hero_dashboard')
    else:
        form = HeroUpdateForm(instance=hero)

    return render(request, "hero_dashboard.html", {
        "hero": hero,
        "assignments": assignments,
        "form": form
    })


@login_required
def support_dashboard(request):
    """
    Dashboard for support staff to view and send messages.
    """
    if request.user.userprofile.role != 'support':
        return HttpResponseForbidden("Access denied")

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(
                sender=request.user,
                content=content,
                timestamp=timezone.now()
            )
            messages.success(request, "Message sent.")

    msgs = Message.objects.order_by('-timestamp')
    return render(request, 'support_dashboard.html', {'messages': msgs})


@login_required
def delete_message(request, message_id):
    """
    Allows a message sender or admin to delete a message.
    """
    msg = get_object_or_404(Message, id=message_id)

    if request.user == msg.sender or request.user.is_staff:
        msg.delete()
        messages.success(request, "Message deleted.")
    else:
        return HttpResponseForbidden("Unauthorized.")

    return redirect('support_dashboard')
