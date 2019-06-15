''' here we import django's function path and all of our
views from the blog application.
for help with creating URLs see Django tutorial page titled django forms'''
from django.urls import path
from . import views
'''Adding URL patterns.'''
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
#name= 'post_list' is the name of the URL that will be used to identify the views
