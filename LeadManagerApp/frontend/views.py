from django.shortcuts import render

# This is where the react gets integrated into django


def index(request):
    return render(request, 'frontend/index.html')
