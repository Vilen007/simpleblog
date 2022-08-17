from django.contrib import admin
from django.urls import path
from . import views
admin.site.site_header="ITTech"
admin.site.site_title = 'My Site Title'
admin.site.index_title = "ITTech"
urlpatterns = [
     # API to post a comment
    path('postComment',views.postComment, name= "postComment"),
    path('', views.blogHome, name= "blogHome"),
    path('<str:slug>', views.blogPost, name= "blogPost"),
   
]
