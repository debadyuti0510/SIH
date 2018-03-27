from django.shortcuts import render
from django.http import HttpResponse
from fir.models import firstruc
from .forms import pnr_form

# Create your views here.
# /response/
def checkpnr(request):
    form = pnr_form()
    if request.method == 'POST':
        form = pnr_form(request.POST)
        if form.is_valid():
            pnrno=form.cleaned_data['pnr']
            phoneno = form.cleaned_data['phone']
            return checkresponse(request, pnrno, phoneno )
    return render(request, 'response/pnr.html',{"form": form})
# /response/123/
def checkresponse(request, pnrno, phoneno):
    all_forms = firstruc.objects.all()
    for form in all_forms:
        if form.pnr == pnrno:
            if form.phone == phoneno:
                break
    context = {
        'form': form,
    }
    return render(request, 'response/checkresponse.html', context)
