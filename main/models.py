from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Hero(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # ✅ Links to user
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    power_level = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=100.00)
    image = models.ImageField(upload_to="hero_images/", blank=True, null=True)

    def __str__(self):
        return self.name


class Hire(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    mission_name = models.CharField(max_length=200)
    date_hired = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.username} hired {self.hero.name}"


class UserProfile(models.Model):
    ROLE_CHOICES = (
        ("client", "Client"),
        ("hero", "Hero"),
        ("support", "Support"),
        ("admin", "Admin"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.hero.name} (x{self.quantity})"


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    stars = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'hero')

    def __str__(self):
        return f"{self.user.username} rated {self.hero.name} {self.stars}★"
