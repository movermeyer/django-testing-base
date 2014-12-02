from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'context_var': 'expected'})

def withUrlFields(request, value):
    return HttpResponse(value)

@login_required
def requiresLogin(request):
    return HttpResponse('')
