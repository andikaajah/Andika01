from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'blog',
        'subjudul':'ini adalah blog kami',
        'benner':'blog/img/benner_blog.jpg',
        'app_css':'blog/css/styles.css',
    }
    return render(request,'index.html', context)