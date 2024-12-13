from django.db import models
from django.contrib.auth.models import User
#from ckeditor.fields import RichTextField
class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    fist_name=models.CharField(max_length=30,null=True)
    last_name=models.CharField(max_length=30,null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    photo_me=models.ImageField(upload_to='photos/my_photo',blank=True)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    



class MySkill(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="photos/skills")
    is_key_skill = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Certificate(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    #image = models.ImageField(blank=True, null=True, upload_to="photos/certificates")
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    
class Project(models.Model):
    #id=models.IntegerField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    #ody = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    slug = models.SlugField(null=True, blank=True)
    url_field = models.URLField(max_length = 200,null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class Blog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    #body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog")
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.name

class ContactProfile(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name",max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f'{self.name}'
    
class Testimonial(models.Model):

    thumbnail = models.ImageField(blank=True, null=True, upload_to="testimonials")
    name = models.CharField(max_length=200, blank=True, null=True)
    institute = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name