from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
import readtime
from django_comments_xtd.models import XtdComment




# create a tuple for the status of each post
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


# each field in this class represents a column in the database table
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    header_image = models.ImageField(null=True,blank=True ,upload_to="images/")
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content =RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tags = TaggableManager()



    # this class contains metadata and uses the created_on field from the model to sort out data which sorts
    # in descending order by default
    class Meta:
        ordering = ['-created_on']

    # this method is the default human-readable representation of the object. Django will use it in many places
    # such as the admin panel
    def __str__(self):
        return self.title
    #def get_absolute_url(self):
    # return reverse("comments", kwargs={"pk": self.pk})

class Comment(models.Model):
    Post = models.ForeignKey(Post,related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    content =models.TextField()
    date_added =models.DateTimeField(auto_now_add=True)

def __str__(self):
    return '%s - %s' % (self.Post.title, self.name)

def get_absolute_url(self):
    return reverse("comment", kwargs={"pk": self.pk})


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

def get_readtime(self):
    result = readtime.of_text(self.content)
    return result.text

#class CustomComment(models.Model):
    #page =Parentalkey(Post, on_delete=models.CASCADE ,releted_name="constomcomments")
    #def save(safe,*args,**kwargs):
       # safe.post =Post.objects.get(pk=safe.object_pk)
      #  super(CustomComment,safe).save(*args,**kwargs)
