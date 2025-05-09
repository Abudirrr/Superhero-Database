from pathlib import Path
import os
import dj_database_url  # 👈 Only needed if you later switch from SQLite to PostgreSQL on Render

# ✅ Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# ✅ Security Key (you should override this in environment variables on Render)
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-x4+3489_%#z((6vcy_f(v%(kq(zgl%%6vd+6g9y&w3m5lep2_v")

# ✅ Debug flag - always False in production
DEBUG = os.getenv("DEBUG", "False") == "True"

# ✅ Allowed hosts
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "superhero-database.onrender.com").split(",")

# ✅ Installed Apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main.apps.MainConfig",  # ✅ Your main app
]

# ✅ Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # ✅ Serve static files on Render
]

# ✅ Root URL
ROOT_URLCONF = "hireahero.urls"

# ✅ Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "main", "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ✅ WSGI application
WSGI_APPLICATION = "hireahero.wsgi.application"

# ✅ Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
    # For PostgreSQL on Render:
    # "default": dj_database_url.config(conn_max_age=600)
}

# ✅ Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ✅ Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ✅ Static & Media files
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "main", "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# ✅ Default primary key
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ✅ Auth redirect
LOGIN_URL = "/login/"

# ✅ Custom error view
CSRF_FAILURE_VIEW = "main.views.error_views.custom_csrf_failure"
