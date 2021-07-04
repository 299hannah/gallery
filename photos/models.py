from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

   
   

    class Meta:
        ordering = ['name']



class Photo(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    location = models.TextField()

    def __str__(self):
        return self.description

    @classmethod
    def search_by_location(cls,search_term):
        photos = cls.objects.filter(location__icontains=search_term)
        return photos
    

