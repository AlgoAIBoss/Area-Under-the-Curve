from django.shortcuts import render, redirect
from plot.models import Plot
from .forms import PlotForm
from .math import *
import os

# Create your views here.

CURRENT_DIR = os.path.dirname(__file__)
model_file = os.path.join(
    CURRENT_DIR, 'static/output.png')


def plot(request):
    if request.method == 'POST':
        form = PlotForm(request.POST)
        if form.is_valid():
            Plot.objects.create(**form.cleaned_data)
            method = form.cleaned_data['method'].method
            function = form.cleaned_data['function']
            start = int(form.cleaned_data['start'])
            end = int(form.cleaned_data['end'])
            split = int(form.cleaned_data['split'])

            if method == 'Simpson':
                area = simpson(function, start, end, split)

            elif method == 'Trapezoid':
                area = trapezoid(function, start, end, split)

            elif method == 'Midpoint':
                area = midpoint(function, start, end, split)
            return redirect("home")

    else:
        form = PlotForm()
    return render(request, 'home.html', {'form': form, "figure": "output.png"})
