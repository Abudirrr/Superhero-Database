from django.urls import path

# ✅ Authentication views
from main.views.auth_views import login_user, logout_user, register_user

# ✅ Dashboards
from main.views.dashboard_views import (
    dashboard, client_dashboard, hero_dashboard,
    support_dashboard, delete_message
)

# ✅ Hero-related views
from main.views.hero_views import (
    home, hero_detail, recommended_heroes,
    hire_page, hire_hero
)

# ✅ Cart functionality
from main.views.cart_views import (
    add_to_cart, view_cart, remove_from_cart
)

# ✅ Profile and rating
from main.views.profile_views import edit_profile
from main.views.rate_views import rate_hero

# ✅ Static and extra pages
from main.views.static_views import about_page, contact_page, match_game

urlpatterns = [
    # ========================
    # Main Pages & Auth
    # ========================
    path("", home, name="home"),
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),

    # ========================
    # Dashboard Views
    # ========================
    path("dashboard/", dashboard, name="dashboard"),
    path("dashboard/client/", client_dashboard, name="client_dashboard"),
    path("dashboard/hero/", hero_dashboard, name="hero_dashboard"),
    path("dashboard/support/", support_dashboard, name="support_dashboard"),
    path("dashboard/support/delete/<int:message_id>/", delete_message, name="delete_message"),

    # ========================
    # Hero Features
    # ========================
    path("hero/<int:hero_id>/", hero_detail, name="hero_detail"),
    path("hire/", hire_page, name="hire"),
    path("hire/<int:hero_id>/", hire_hero, name="hire_hero"),
    path("recommendations/<int:hero_id>/", recommended_heroes, name="recommended_heroes"),

    # ========================
    # Cart Functionality
    # ========================
    path("cart/", view_cart, name="view_cart"),
    path("cart/add/<int:hero_id>/", add_to_cart, name="add_to_cart"),
    path("cart/remove/<int:item_id>/", remove_from_cart, name="remove_from_cart"),

    # ========================
    # Profile & Ratings
    # ========================
    path("edit-profile/", edit_profile, name="edit_profile"),
    path("rate/", rate_hero, name="rate_hero"),

    # ========================
    # Static Pages
    # ========================
    path("game/", match_game, name="game"),
    path("about/", about_page, name="about"),
    path("contact/", contact_page, name="contact"),
]
