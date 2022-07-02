from django.urls import path

from .views import  index_view,create,delete,update

urlpatterns = [
    path('', index_view, name='index_view'),
    path('create', create),
    path('update/<int:id>', update),
    path('delete/<int:id>', delete),
]