from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Automatically create a UserProfile when a new User is created.
    Supports assigning a role if attached as _created_role by the registration form.
    Defaults to 'client' if no role is set.
    """
    if created and not hasattr(instance, 'userprofile'):
        # Get the role passed during registration or fallback to 'client'
        role = getattr(instance, '_created_role', 'client')
        UserProfile.objects.create(user=instance, role=role)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Ensures the UserProfile is saved every time the User is saved.
    """
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()
