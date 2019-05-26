from django.urls import path
from .views import CrudView,delete,update
urlpatterns = [
    path('',CrudView.as_view(),name='home'),
    path('delete/<int:id>',delete,name='delete'),
    path('update/<int:id>',update,name='update')
]