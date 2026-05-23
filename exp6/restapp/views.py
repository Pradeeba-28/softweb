from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def adminpage(request):
    return render(request, 'admin.html')

def contact(request):
    return render(request, 'contact.html')
