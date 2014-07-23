from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. Your bill is near!")

# Create your views here.
