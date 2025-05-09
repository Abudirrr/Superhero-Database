from pathlib import Path
import os

# ✅ Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# ✅ Secret key (from environment for security)
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-x4+3489_%#z((6vcy_f(v%(kq(zgl%%6vd+6g9y&w3m5lep2_v")

# ✅ Detect Render deployment
RENDER = os.environ.get("RENDER", "") == "true"

# ✅ Debug mode (True locally, False on Render)
DEBUG = not RENDER  # Optional: use env var if needed

# ✅ Allowed Hosts
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.onrender.com']

# ✅ Installed Applications
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main.apps.MainConfig",
]

# ✅ Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # ✅ Serves static files in prod
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ✅ Root URLs and WSGI
ROOT_URLCONF = "hireahero.urls"
WSGI_APPLICATION = "hireahero.wsgi.application"

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

# ✅ SQLite Database (fine for development and Render demo)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
    # To use PostgreSQL on Render:
    # "default": dj_database_url.config(conn_max_age=600)
}

# ✅ Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ✅ Localization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ✅ Static Files (CSS, JS)
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "main", "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ✅ Media Files (user-uploaded images like hero photos)
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# ✅ Primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ✅ Login Redirects
LOGIN_URL = "/login/"

# ✅ CSRF Custom Handler
CSRF_FAILURE_VIEW = "main.views.error_views.custom_csrf_failure"
