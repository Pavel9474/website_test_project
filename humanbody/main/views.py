from django.shortcuts import render

# Create your views here.
def index(request):
    data={'title':'Главная страница!!',
          'values':['Some','hello','pahan'],
          'obj':{'car': 'BMV',
              'age':18,
              'bone':'femur'}
          }
    return render(request,'main/index.html', data)
def about(request):
    return render(request,"main/about.html")