from django.shortcuts import render

def handler404(request, exception):
    return render(request, "error.html", {
        "status_code": 404,
        "message": "Page not found. Please check the URL or return to the homepage."
    }, status=404)

def handler500(request):
    return render(request, "error.html", {
        "status_code": 500,
        "message": "Something went wrong on our end. We're fixing it!"
    }, status=500)

def handler403(request, exception):
    return render(request, "error.html", {
        "status_code": 403,
        "message": "You are not authorized to access this page."
    }, status=403)

def custom_csrf_failure(request, reason=""):
    return render(request, "error.html", {
        "status_code": 403,
        "message": "Security check failed. Please refresh and try again."
    }, status=403)
