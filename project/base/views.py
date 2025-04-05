from django.shortcuts import redirect, render

from project.base.forms import CadastroForm


# Create your views here.

def home(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if not form.is_valid():
            return render(request, 'base/home.html', {'form': form})
        return redirect('https://google.com')    
    
    form = CadastroForm()
    return render(request, 'base/home.html', {'form': form, 'teste': None})
