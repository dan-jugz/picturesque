from django.test import TestCase
from .models import Location,Category,Image

class TestModelImages(TestCase):

    def setUp(self):
        self.categ = Category(category = "travels")
        self.categ.save()
        self.locate = Location(location = "mombasa",date_taken = "2019-10-04")
        self.locate.save()
        self.new_image = Image(image = "tesla.png",image_name = "tesla",image_description = "cool picture",image_post_date = "2019-10-o4",image_photographer = "denis",category = self.categ,location = self.locate)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_image(self):
        self.new_image.save_image()
        image_length = Image.objects.all()
        self.assertTrue(len(image_length) > 0)

    def tearDown(self):
        Image.objects.all().delete()

    def test_delete_image(self):
        self.new_image.save_image()
        self.another_image = Image(image = "fj_cruiser.png",image_name = "fj_cruiser",image_description = "cool picture",image_post_date = "2019-10-o4",image_photographer = "munene",category = self.categ,location = self.locate)
        self.another_image.save_image()
        self.new_image.delete_image()
        dt = Image.objects.all()
        self.assertEqual(len(dt),1)

    def test_display_images(self):
        self.new_image.save_image()
        self.another_image = Image(image = "fj_cruiser.png",image_name = "fj_cruiser",image_description = "cool picture",image_post_date = "2019-10-o4",image_photographer = "munene",category = self.categ,location = self.locate)
        self.another_image.save_image()
        dt = Image.display_images()
        self.assertEqual(len(dt),2)


    def test_search(self):
        self.new_image.save_image()
        self.another_image = Image(image = "fj_cruiser.png",image_name = "fj_cruiser",image_description = "cool picture",image_post_date = "2019-10-o4",image_photographer = "munene",category = self.categ,location = self.locate)
        self.another_image.save_image()
        search_term = "cars"
        search1 = Image.search(search_term)
        search2 = Image.objects.filter(image_name__icontains = search_term)
        self.assertEqual(len(search2),len(search1))
  
    def test_search_category(self):
        self.new_image.save_image()
        self.another_image = Image(image = "fj_cruiser.png",image_name = "fj_cruiser",image_description = "cool picture",image_post_date = "2019-10-o4",image_photographer = "munene",category = self.categ,location = self.locate)
        self.another_image.save_image()
        searched_category = "travels"
        searched_images = Image.search_category(searched_category)
        self.assertEqual(len(searched_images),2)

    def test_str(self):
        self.new_image.save_image()
        self.another_image = Image(image = "fj_cruiser.png",image_name = "fj_cruiser",image_description = "cool picture",image_post_date = "2019-10-o4",image_photographer = "munene",category = self.categ,location = self.locate)
        self.another_image.save_image()
        result = Image.objects.filter(image_name = "fj_cruiser")
        final = self.another_image.__str__()
        self.assertEqual(final,result[0].image_name)
        
    
class TestLocation(TestCase):
    def setUp(self):
        self.new_location = Location(location = "dubai",date_taken = "2019-10-04")

    def test_locationInstance(self):
        self.assertTrue(isinstance(self.new_location,Location))


    def test_save_location(self):
        self.new_location.save_location()
        location_length = Location.objects.all()
        self.assertTrue(len(location_length) > 0)

    def test_display_locations(self):
        self.new_location.save_location()
        all_locations = Location.display_locations()
        self.assertEqual(len(all_locations),1)


class TestCategory(TestCase):
    def setUp(self):
        self.new_category = Category(category = "adventure")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,Category))

    def test_save(self):
        self.new_category.save_category()
        self.assertTrue(len(Category.objects.all()) > 0)