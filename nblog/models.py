from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
from django.utils.text import slugify

from taggit.models import Tag
#from reading_time.utils import reading_time
#from reading_time.reading_time import reading_time





# create a tuple for the status of each post
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


'''class Tag(models.Model):
    name = models.CharField(max_length=50,unique=True)
    slug =models.SlugField(max_length=100,unique=True)
    def save(self,*args,**kwargs):
        if self.pk:
            self.slug=slugify(self.name)
        if self.slug or not self.slug:
            self.slug=slugify(self.name)
        super().save(*args,**kwargs)
    def get_post_tag_url(self):
        return reverse('post_tag',kwargs={'slug':self.slug})'''
# each field in this class represents a column in the database table
'''class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    header_image = models.ImageField(null=True,blank=True ,upload_to="images/")
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nblog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content =RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tag = models.ManyToManyField(Tag,blank=True,related_name='tags')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)'''
    

class Category(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nblog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    #tag = TaggableManager
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, related_name='posts')
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
   # read_time = models.IntegerField(default=0)
def get_post_tag_url(self, tag_slug):
    return reverse('post_list_by_tag', args=[str(tag_slug)])



  
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])




    # this class contains metadata and uses the created_on field from the model to sort out data which sorts
    # in descending order by default
    class Meta:
        ordering = ['-created_on']

    # this method is the default human-readable representation of the object. Django will use it in many places
    # such as the admin panel
    def __str__(self):
        return self.title
def related_posts(self):
        related_posts = Post.objects.filter(tags__in=self.tags.all()).exclude(id=self.id).distinct()[:4]
        return related_posts


class SubscribedUsers(models.Model):
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.email

class CustomUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.email


class Order(models.Model):
    pass

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)




class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name









    

