from django.test import TestCase
from .models import Profile,Comments,Image
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    
    # Setup method
    def setUp(self):
        self.user = User.objects.create(id = 1,username = 'Aggy')
        self.profile = Profile(firstname = 'Reina',lastname = 'Aggy',profile_photo = 'p1.jpeg', bio = 'cool',date = '12.11.2019', user = self.user)
 
    # Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    # testing the save method
    def test_save_method(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) >= 1)
        
    def test_delete_method(self):
       self.profile.save_profile()

    def test_update_method(self):
        self.profile.save_profile()
        new_profile = Profile.objects.filter(bio = 'cool').update(bio = 'kind')

class CommentTestClass(TestCase):
     # Setup method
    def setUp(self):
        self.comment = Comments.objects.create(comment = 'woooowww')
        
    # Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))

    # testing the save method
    def test_save_method(self):
        self.comment.save_comments()
        comment = Comments.objects.all()
        self.assertTrue(len(comment) > 0)
        
    def test_delete_method(self):
        self.comment.save_comments()
        self.comment.delete_comments()
        comment = Comments.objects.all()
        self.assertTrue(len(comment) >= 0)

class ImageTestClass(TestCase):
    
    # Setup method
    def setUp(self):
        self.image = Image(image = 'dog2.jpg', image_name='test',image_caption='This is a test image',date = '12.9.2019')
        
        
    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()

    # Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
        
    # testing the save method
    def test_save_method(self):
        self.image = Image(image = 'dog2.jpg', image_name='test',image_caption='This is a test image',date = '12.9.2019')
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) >= 1)
        
    def test_delete_method(self):
        self.image = Image(image = 'dog2.jpg', image_name='test',image_caption='This is a test image',date = '12.9.2019')
        self.image.save_image()
        images = self.image.delete_image()
        deleted = Image.objects.all()
        self.assertTrue(len(deleted) <= 0)