from django.shortcuts import render
from uploader.models import Problem
# Create your views here.


def home(request):
    lst = Problem.objects.all()

    return render(request, 'index.html', {'objs': lst})
