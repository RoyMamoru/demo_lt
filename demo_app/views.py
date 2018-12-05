from django.shortcuts import render
from .forms import InputForm
from django.shortcuts import redirect

# Create your views here.
def base(request):
    return render(request, 'demo_app/base.html', {})

# 自前で書いたForm
def input(request):
    return render(request, 'demo_app/input.html', {})

# Form画面
def input_form(request):
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('result')
    else:
        form = InputForm()
        return render(request, 'demo_app/input_form.html', {'form':form})


def result(request):
    return render(request, 'demo_app/result.html', {})
