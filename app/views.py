from django.shortcuts import render
from app.models import Student


def index(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        s = Student(firstname=fname, email=email, message=message)
        s.save()

    return render(request, 'app/index.html')


def interaction(request):
    return render(request, 'app/mainpage.html')
