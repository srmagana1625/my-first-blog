''' here we import django's function path and all of our
views from the blog application.'''
from django.urls import path
from . import views
'''Adding URL patterns.'''
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail')
]
#name= 'post_list' is the name of the URL that will be used to identify the views
