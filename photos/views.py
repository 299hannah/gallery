from django.shortcuts import render
from .models import Category, Photo

# Create your views here.
def index(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()

    context = {'categories': categories, 'photos':photos}
    
    return render(request, 'index.html', context)

def photos(request, pk):
    photo = Photo.objects.get(id=pk)

    return render(request, 'photos.html',{'photo':photo})
