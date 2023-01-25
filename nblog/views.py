

from django.shortcuts import render, redirect
from django.views import generic
from .models import Post, Comment
from django.views.generic.detail import DetailView
from .form import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import SubscribedUsers
from django.contrib import messages
from django.core.mail import EmailMessage
from .form import NewsletterForm
from django.views.decorators.csrf import csrf_exempt
import uuid
from django.contrib.auth import get_user_model
from django.urls import reverse
from  django . core.mail import send_mail
from django_pandas.io import read_frame



from django.contrib import messages
from django.conf import settings

from paypal.standard.forms import PayPalPaymentsForm
from django.db.models import Q

#from .decorators import user_is_superuser








class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'nblog/index.html'  # a list of all posts will be displayed on index.html


class PostDetail(generic.DetailView):
       model = Post
       template_name = 'nblog/post_detail.html'  # detail about each blog post will be on post_detail.

def contact_form(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Message from {form.cleaned_data["name"]}'
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["email"]
            recipients = ['saahndongransom@gmail.com']
            try:
                send_mail(subject, message, sender, recipients, fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponse('Success...Your email has been sent')
    return render(request, 'nblog/contact.html', {'form': form})
    return redirect('/')

def policy(request):
    return render(request , 'nblog/policy.html',{'policy': policy} )
def site(request):
    return render(request, 'nblog/site.html',{'site': site})
def aboutme(request):
    return render(request,'nblog/aboutme.html',{'aboutme':aboutme})
def footer(request):
    return render(request,'nblog/footer.html',{'footer':footer})

def subscribe(request):
    print(request.method)
    print(request.method, "method")
    if request.method == 'POST':
        email = request.POST.get('email')

        if not email:
            messages.error(request, "You must type legit name and email to subscribe to a Newsletter")
            return redirect("/")

        if get_user_model().objects.filter(email=email).first():
            print(f"Found registered user with associated {email} email. You must login to subscribe or unsubscribe.")
            messages.error(request, f"Found registered user with associated {email} email. You must login to subscribe or unsubscribe.")
            return redirect(request.META.get("HTTP_REFERER", "/"))

        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            print(f"{email} email address is already subscriber.")
            messages.error(request, f"{email} email address is already subscriber.")
            return redirect(request.META.get("HTTP_REFERER", "/"))

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = SubscribedUsers(email=email)
        subscribe_model_instance.save()
        messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
        return redirect(request.META.get("HTTP_REFERER", "/"))








 #paypal
def feli(request):
    host = request.get_host()
    paypal_dict = {
            'business':settings.PAYPAL_RECEIVER_EMAIL,
            'amount': '%.20.0f',
            'item_name': "product 1",
            'invoice': "str(uuid.uuid4())",
            'currency_code': 'USD',
            'notify_url':f'http://{host}{reverse("paypal-ipn")}',
            'return_url':f'http://{host}{reverse("paypal-return")}',
            'cancel_return':f'http://{host}{reverse("paypal-cancel")}',


    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    contact = {'form':form}
    return render(request,'nblog/feli.html',contact)

def paypal_return(request):
    messages.success(request="you/ succefully make payment")
    return redirect('home')

def paypal_cancel(request):
    messages.error(request="you/ succefully make payment")
    return redirect('home')





def newsletter(request):
    
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            receivers = form.cleaned_data.get('receivers').split(',')
            email_message = form.cleaned_data.get('message')

            mail = EmailMessage(subject, email_message, f"nblog <{request.user.email}>", bcc=receivers)
            mail.content_subtype = 'html'

            if mail.send():
                subject = form.cleaned_data.get('subject')
                message = form.cleaned_data.get('message')
                send_mail(
    subject,
    message,
    '',
    ['saahrm@yahoo.com'],
    fail_silently=False,
)
                messages.success(request, "Email sent succesfully")
            else:
                messages.error(request, "There was an error sending email")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

        return redirect('/')

    form = NewsletterForm()
    form.fields['receivers'].initial = ','.join([active.email for active in SubscribedUsers.objects.all()])
    return render(request=request, template_name='nblog/newsletter.html', context={'form': form})

def get_content_data(self, **kwargs):
        similar_posts = self.object.tags.similar_objects()[:3]
        post_comments_count = Comment.objects.all().filter(post=self.object.id).count()
        post_comments = Comment.objects.all().filter(post=self.object.id)
        content = self.super().get_content_data(**kwargs)
        content.update({
            "similar_posts":similar_posts,
            'form': self.forms,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
        })


        return content


def get_absolute_url(self):
    return reverse("comment", kwargs={"pk": self.pk})
def home1(request):
   return render(request,'nblog/home1.html',{'home1':home1})


def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query) | Q(content__icontains=query)

            results= Post.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'search/search.html', context)

        else:
            return render(request, 'search/search.html')

    else:
        return render(request, 'search/search.html')
    
def reply(request):
   return render(request,'nblog/reply.html',{'reply':reply})

    