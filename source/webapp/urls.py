from django.urls import path

from .views import  index_view,create,delete,update

urlpatterns = [
    path('', index_view, name='index_view'),
    path('create', create),
    path('update', update),
    path('delete', delete),
]