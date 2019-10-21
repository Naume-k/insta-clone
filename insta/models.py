from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    firstname = models.CharField(max_length =30)
    lastname = models.CharField(max_length =30)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to = 'profile_photos/', null=True)
    bio = HTMLField()
    date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_all_instagram_users(cls):
        instagram_users = cls.objects.all()
        return instagram_users

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_profile(cls,id,value):
        cls.objects.filter(id = id).update(user_id = new_user)

    @classmethod
    def search_by_profile(cls,username):
        certain_user = cls.objects.filter(user__username__icontains = username)
        return certain_user

def __str__(self):
        return self.user

class Image(models.Model):
    '''
    a class for Image model
    '''
    image_caption = models.CharField(max_length =30)
    image_name = models.CharField(max_length =30,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to = 'uploads/', null=True)
    date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE ,null=True)
    likes= models.IntegerField(default=0)

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all().prefetch_related('comments_set')
        return images

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(cls,id,caption):
        update_image = cls.objects.filter(id = id).update(image_caption = caption)
        return update_image

    def __str__(self):
        return self.image_caption

# class Preference(models.Model):
#     '''
#     http://www.learningaboutelectronics.com/Articles/How-to-add-like-dislike-buttons-to-a-post-Python-Django.php
#     '''
#     user= models.ForeignKey(User)
#     post= models.ForeignKey(Image)
#     value= models.IntegerField()
#     date= models.DateTimeField(auto_now= True)

    
#     def __str__(self):
#         return str(self.user) + ':' + str(self.post) +':' + str(self.value)

#     class Meta:
#        unique_together = ("user", "post", "value")

class Comments(models.Model):
    comment = models.CharField(max_length = 250)
    posted_by = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True)
    commented_image = models.ForeignKey(Image, on_delete=models.CASCADE, null = True)

    def save_comments(self):
        self.save()

    def delete_comments(self):
        self.delete()
    
    def update_comment(self):
        self.update()

def __str__(self):
        return self.posted_by

class Followers(models.Model):
    '''
    https://stackoverflow.com/questions/27587216/get-the-follower-count-in-django
    '''    
    from_user = models.ForeignKey(User, related_name='following_set', null = True)
    to_user = models.ForeignKey(User, related_name='follower_set', null = True)

