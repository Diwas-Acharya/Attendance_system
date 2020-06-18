
from django.urls import path , include
from . import views


urlpatterns = [
   path('',views.home),
   path('ser_reg',views.ser_reg),
   path('finder', views.finder),
   path("make_present/<int:myid>",views.make_present)
]
