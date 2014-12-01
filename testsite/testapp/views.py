from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def requiresLogin(request):
    return HttpResponse('')
