from django.http import HttpResponse

def index(request):
    return HttpResponse('HELLO, it is blog!')
# Create your views here.
