from django.shortcuts import render, redirect
from .models import Bonedata
from .forms import BonedataForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django_table_sort.table import TableSort

# Create your views here.



def databones_home(request):
    show_bone_parameters=Bonedata.objects.order_by('year_pub')
    return render(request,'databones/databones_home.html', {'show_bone_parameters': show_bone_parameters})

def tablesort(request):
    table=Bonedata.objects.all()
    return render(request, "databones/databones_home.html", context={"table": table})

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
class ListViewExample(ListView):
    model = Bonedata
    template_name: str = "databones_home.html"
    ordering_key = "o"

    def get_ordering(self) -> tuple:
        return self.request.GET.getlist(self.ordering_key, None)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["table"] = TableSort(
            self.request,
            self.object_list,
            table_css_classes="table table-light table-striped table-sm",
            sort_key_name=self.ordering_key,
        )
        return context
