from django.db import models
import datetime as time

class Location(models.Model):
    location = models.CharField(max_length=60)
    date_taken = models.DateTimeField(auto_now_add=True)

    def save_location(self):
        self.save()


    def __str__(self):
        return self.location


    @classmethod
    def display_locations(cls):
        locations = cls.objects.all()
        return locations


class Category(models.Model):
    category = models.CharField(max_length=60)

    def save_category(self):
        self.save()

    def __str__(self):
        return self.category



class Image(models.Model):
    image = models.ImageField(upload_to='pictures/')
    image_name = models.CharField(max_length = 60)
    image_description = models.TextField()
    image_post_date = models.DateTimeField(auto_now_add=True)
    image_photographer = models.CharField(max_length=60,blank=True)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    location = models.ForeignKey(Location,on_delete = models.CASCADE)

    def save_image(self):
        self.save()

    def __str__(self):
        return self.image_name

    def delete_image(self):
        self.delete()


    @classmethod
    def display_images(cls):
        images = cls.objects.all()
        return images

    
    @classmethod
    def search_category(cls,searched_category):
        get_cate_id = Category.objects.filter(category__icontains = searched_category)
        ids = len(get_cate_id) 
        all_images = []
        for an_id in range(ids):
            images = cls.objects.filter(category__in = [get_cate_id[an_id].id])
            all_images.append(images)
        return all_images

        