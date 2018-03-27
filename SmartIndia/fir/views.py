from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import firstruc
from .forms import fir_form
# Create your views here.

def firform(request):
    form = fir_form(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        "form": form,
    }
    return render(request, 'fir/firform.html',context)
