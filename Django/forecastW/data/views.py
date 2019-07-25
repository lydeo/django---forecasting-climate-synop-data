from django.shortcuts import render
from .models import data_klimat

def index(request):
    posts = data_klimat.objects.all()
    context ={
        'Posts':posts,
    }
    if request.method =='POST':
        context['case'] = request.POST['jenis_data']
    return render(request,'data_views.html',context)