from django.http import HttpResponse

def start(request):
    return HttpResponse('django already!')