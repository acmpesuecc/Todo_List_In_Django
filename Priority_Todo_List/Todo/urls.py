from django.urls import path, include
from . import views

urlpatterns = [
    # Todo - create path to index view
    path('', views.index , name='index'),
    # Todo - create path to add view
    path('add/',views.add , name='add'),
    # Todo - create path to delete view, must take 'id'(integer) as parameter in url
    path('delete/', views.delete , name='delete')
]
