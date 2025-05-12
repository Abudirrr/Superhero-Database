from pathlib import Path
import os
import pymysql
pymysql.install_as_MySQLdb()

# === Base directory ===
BASE_DIR = Path(__file__).resolve().parent.parent

# === Security settings ===
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# ✅ Allowed hosts for production and development
ALLOWED_HOSTS = [
    "hireahero-production.up.railway.app",
    "*.railway.app"
]
if DEBUG:
    ALLOWED_HOSTS.extend(["localhost", "127.0.0.1"])

# === Installed apps ===
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main.apps.MainConfig",
]

# === Middleware ===
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# === URL and WSGI ===
ROOT_URLCONF = "hireahero.urls"
WSGI_APPLICATION = "hireahero.wsgi.application"

# === Templates ===
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

# ✅ MySQL Database Configuration (uses Railway env vars)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("MYSQL_DATABASE"),
        "USER": os.getenv("MYSQL_USER"),
        "PASSWORD": os.getenv("MYSQL_PASSWORD"),
        "HOST": os.getenv("MYSQL_HOST"),
        "PORT": os.getenv("MYSQL_PORT", "3306"),
        "OPTIONS": {
            "ssl": {"ssl-mode": "REQUIRED"}
        }
    }
}

# === Password validation ===
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# === Internationalization ===
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# === Static files ===
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "main", "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# === Media files ===
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# === Auth redirects ===
LOGIN_URL = "/login/"

# === CSRF / Security headers ===
CSRF_TRUSTED_ORIGINS = [
    "https://hireahero-production.up.railway.app",
    "https://*.railway.app"
]
if DEBUG:
    CSRF_TRUSTED_ORIGINS.append("http://127.0.0.1")

CSRF_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# === Auto field setting ===
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# === Optional CSRF failure view ===
CSRF_FAILURE_VIEW = "main.views.error_views.custom_csrf_failure"
