from django.shortcuts import render, redirect
from .models import Bonedata
from .forms import BonedataForm
# Create your views here.
def databones_home(request):
    show_bone_parameters=Bonedata.objects.order_by('year_pub')
    return render(request,'databones/databones_home.html', {'show_bone_parameters': show_bone_parameters})

def create(request):
    error= ''
    if request.method == 'POST':
        form=BonedataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = BonedataForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'databones/create.html', data)