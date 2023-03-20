from .import views

#from nblog.views import LoadMorePostsView
#from .views import add_featured_post
from django.urls import path , include
from .views import contact_success,contact





urlpatterns = [
    
    path('footer.html',views.footer,name='footer'),
    path("newsletter", views.newsletter, name="newsletter"),
    path('', views.PostList.as_view(), name='home'),

    #path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('<int:pk>', views.PostDetail, name='post_detail'),
    path('<slug:slug>', views.post_tag, name='post_tag'),
    #path('contact/', views.contact_form, name='contact'),
    path('policy/', views.policy, name='policy'),
    path('mission.html',views.mission,name='mission'),
    path('newhatchtech.html',views.site, name='newhatchtech'),
    path('aboutme.html',views.aboutme,name='aboutme'),
    path('subscribe/', views.subscribe, name='subscribe_newsletter'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('home1/', views.home1, name="home1"),
    path('feli.html',views.feli,name='feli'),
    path('paypal_return/', views.paypal_return,name='paypal-return'),
    path('paypal-cancel/', views.paypal_cancel,name='paypal-cancel'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    #path('', views.post_list_view, name='home'),
    #path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    #path('post/<int:pk>/add_comment_to_post/', views.add_comment_to_post, name='add_comment_to_post'),
    


  

    #path('categories/', category_list, name='category_list'),
   
    #path('load-more-posts/', LoadMorePostsView.as_view(), name='load_more_posts'),

    #path('load-more/', views.post_list, name='load-more'),
    #path('users/', include('users.urls')),
    #path('',views.home1, name='home1'),
   # path('tag/<slug:tag_slug>',views.PostList, name='PostList_by_tag'),
    path('category/<str:category_name>/', views.CategoryView.as_view(), name='category'),


     
    path('category/<slug:slug>/', views.category, name='category'),
 
   
#path('contact/', views.contact_form, name='contact'),
    path('contact/', contact, name='contact'),
    #path('contact_success/', contact_success, name='contact_success'),
    path('contact/success/', contact_success, name='contact_success'),
]

  
   





