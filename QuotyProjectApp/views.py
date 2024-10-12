from django.shortcuts import render

app_name = 'QuotyProjectApp'

# Create your views here.
def index(request):
    return render(request, 'index.html')

def details(request):
    return render(request, 'details.html')


def pay(request):
    return render(request, 'pay.html')

def contact(request):
    return render(request, 'contact.html')

