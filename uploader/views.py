from django.shortcuts import render

from uploader.forms import ProblemForm

# Create your views here.


def addProblem(request):
    form = ProblemForm

    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'add-problem.html', context)
