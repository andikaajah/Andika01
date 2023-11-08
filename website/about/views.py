from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'judul':'About',
        'subjudul':'ini adalah about',
        'benner':'about/img/benner_about.jpg',
        'app_css':'about/css/styles.css',
    }
    return render(request, 'index.html',context)