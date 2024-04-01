from django.shortcuts import render, redirect
from .models import Bonedata
from .forms import BonedataForm
from django.views.generic import DetailView, UpdateView, DeleteView
# Create your views here.



def databones_home(request):
    show_bone_parameters=Bonedata.objects.order_by('year_pub')
    return render(request,'databones/databones_home.html', {'show_bone_parameters': show_bone_parameters})

class databones_Detailviev(DetailView):
    model = Bonedata
    template_name='databones/details_view.html'
    context_object_name= 'article'

class databones_Updateviev(UpdateView):
    model = Bonedata
    template_name='databones/create.html'
    form_class = BonedataForm

class databones_Deleteviev(DeleteView):
    model = Bonedata
    success_url= '/databones/'
    template_name= 'databones/databones-delete.html'
    

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