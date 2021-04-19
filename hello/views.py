from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello, Cool IT Help!")