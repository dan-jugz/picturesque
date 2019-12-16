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


