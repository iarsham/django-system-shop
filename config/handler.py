from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def custom404(request, exception):
    return render(request, 'handlers/404.html')
