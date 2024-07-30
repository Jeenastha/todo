from django.urls import path
from .import views

urlpatterns = [
    path('get_blog/',views.get_blog),
    path('filter_with_s/',views.filter_with_s),
    path('home/',views.home),
    path('authors/',views.get_author)
]

