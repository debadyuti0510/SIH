from django.shortcuts import render
from django.http import HttpResponse
from .forms import policelogin
from fir.models import firstruc

# Create your views here.

def login(request):
    form = policelogin()
    if request.method == 'POST':
        form = policelogin(request.POST)
        if form.is_valid():
            return responselist(request)
    return render(request, 'police/policeadmin.html',{"form": form})

def responselist(request):
    all_forms = firstruc.objects.all()
    return render(request, 'police/responselist.html', {"all_forms": all_forms})

def firdisplay(request,phoneno):
    all_forms = firstruc.objects.all()
    for form in all_forms:
        if form.phone == phoneno:
            break
    context = {
        'form': form,
    }
    return render(request, 'response/checkresponse.html', context)
