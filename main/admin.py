from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Hero, Category, Hire, UserProfile, Message, CartItem, Rating


# ✅ Inline UserProfile in User admin (editable + deletable)
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = True  # ✅ Allows profile deletion when user is deleted
    verbose_name_plural = 'Profile'
    fk_name = 'user'


# ✅ Custom User admin with role column and full delete access
class CustomUserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_role', 'is_staff')
    list_select_related = ('userprofile',)

    def get_role(self, instance):
        return instance.userprofile.role if hasattr(instance, 'userprofile') else '—'
    get_role.short_description = 'Role'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('userprofile')


# 🔁 Replace default User admin with our custom version
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


# ✅ Message Admin
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("sender", "content", "timestamp")
    search_fields = ("sender__username", "content")
    ordering = ("-timestamp",)
    list_filter = ("timestamp",)


# ✅ Hero Admin
@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "available", "power_level")
    list_filter = ("available", "category")
    search_fields = ("name", "description")
    ordering = ("-power_level",)


# ✅ Category Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


# ✅ Hire Admin (deletion enabled)
@admin.register(Hire)
class HireAdmin(admin.ModelAdmin):
    list_display = ("client", "hero", "mission_name", "date_hired")
    list_filter = ("hero", "date_hired")
    search_fields = ("client__username", "hero__name", "mission_name")
    ordering = ("-date_hired",)
    actions = ['delete_selected']  # ✅ Allows bulk delete


# ✅ UserProfile Admin (if accessed directly)
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role")
    list_filter = ("role",)
    search_fields = ("user__username",)
    ordering = ("role", "user__username")


# ✅ CartItem Admin
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("user", "hero", "quantity")
    search_fields = ("user__username", "hero__name")
    ordering = ("user__username",)


# ✅ Rating Admin
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("user", "hero", "stars")
    list_filter = ("stars",)
    search_fields = ("user__username", "hero__name")
    ordering = ("-stars",)
