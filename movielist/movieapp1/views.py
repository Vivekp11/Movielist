from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie
from .forms import movie_form


# Create your views here.
def index(request):
    obj = movie.objects.all()

    return render(request, 'index.html', {'result': obj})


def details(request, movie_id):
    moviee = movie.objects.get(id=movie_id)
    return render(request, 'details.html', {'result': moviee})


def addmovie(request):
    if request.method == 'POST':
        name = request.POST.get('movie_name')
        image = request.FILES['movie_image']
        desc = request.POST.get('movie_desc')
        Movie = movie(name=name, image=image, desc=desc)
        Movie.save()
        return redirect('/')
    return render(request, 'addmovie.html')

def update(request, movie_id):
    mov = movie.objects.get(id=movie_id)
    form = movie_form(request. POST or None, request.FILES, instance=mov)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': mov})

def delete(request, m_id):
    if request.method == 'POST':
        mov = movie.objects.get(id=m_id)
        mov.delete()
        return redirect('/')

    return render(request, 'delete.html')



