from django.db import models
from ckeditor.fields import RichTextField
from accounts.models import CustomUser as User
from django.forms import ModelForm
from django import forms
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    body=RichTextField(blank=True,null=True)
    image = models.ImageField(upload_to='posts_images')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Blogform(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'subtitle', 'image','body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your title'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control col-lg-12'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }


class comment(models.Model):
    body=models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    commented_post=models.ForeignKey(Blog, related_name='comments' ,on_delete=models.CASCADE)


    def __str__(self):
      return self.body





