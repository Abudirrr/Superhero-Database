from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile, Hero, Category


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Automatically create a UserProfile when a new User is created.
    If the role is 'hero', also create a Hero object linked to that user.
    """
    if created and not hasattr(instance, 'userprofile'):
        raw_role = getattr(instance, '_created_role', 'client')
        role = str(raw_role).strip().lower()

        if role not in ['client', 'hero', 'support']:
            role = 'client'

        # Create the profile
        profile = UserProfile.objects.create(user=instance, role=role)

        # If role is hero, also create a Hero record
        if role == 'hero':
            default_category = Category.objects.first()
            if default_category:
                Hero.objects.create(
                    user=instance,
                    name=instance.username,
                    description="This hero has no description yet.",
                    category=default_category,
                    available=True,
                    power_level=1,
                    price=100.00
                )


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Ensures the UserProfile is saved every time the User is saved.
    """
    try:
        instance.userprofile.save()
    except UserProfile.DoesNotExist:
        pass
