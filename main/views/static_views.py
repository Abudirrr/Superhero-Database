from django.shortcuts import render

def match_game(request):
    return render(request, 'game.html')

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    return render(request, 'contact.html')
