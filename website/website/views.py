from django.shortcuts import render

def index(request):
    context = {
        'judul':'website dika',
        'subjudul':'Selamat datang di website saya',
        'benner':'img/benner_home.jpg',
    }
    return render(request, 'index.html', context)