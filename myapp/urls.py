from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.testfn,name='home'),
    path('test',views.testfn2,name='test'),
    path('test1',views.testfn3,name='test1')
]
