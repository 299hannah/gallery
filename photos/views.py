from django.shortcuts import render
from .models import Category, Photo

# Create your views here.
def index(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)


        
    categories = Category.objects.all()

    context = {'categories': categories, 'photos':photos}
    
    return render(request, 'index.html', context)

def photos(request, pk):
    photo = Photo.objects.get(id=pk)

    return render(request, 'photos.html',{'photo':photo})
