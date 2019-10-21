from django import forms
from .models import Profile,Image,Comments

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'date', 'firstname', 'lastname']
        

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['image_name', 'profile_pic','date','user', 'likes','profile']
      

class commentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['commented_image', 'posted_by','profile']
       