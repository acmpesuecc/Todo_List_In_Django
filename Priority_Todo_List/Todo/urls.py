from django.urls import path, include
from . import views

urlpatterns = [
    # Todo - create path to index view
    path('', , name='index'),
    # Todo - create path to add view
    path('add/', , name='add'),
    # Todo - create path to delete view, must take 'id'(integer) as parameter in url
    path('delete/', , name='delete')
]
