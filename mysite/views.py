from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Django REST API! Visit /api/ for the API endpoints.")
