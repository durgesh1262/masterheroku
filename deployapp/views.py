from django.shortcuts import render
from .models import DeployModel
from .forms import DeployHerokoForm

def Deployview(request):
    if request.method == 'POST':
        fm = DeployHerokoForm(request.POST)
        if fm.is_valid():
            fm.save()
            return render(request, 'thanks.html', {'form':fm})
    else:
        fm = DeployHerokoForm()
    return render(request, 'adddata.html', {'form':fm})         

# Create your views here.
