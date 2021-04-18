from django.urls import path 
from .views import Home, delete ,Login,Logout

urlpatterns = [ 
    path('',Home),
    path('delete/<int:id>',delete),
    path('login/',Login),
    path('logout/',Logout)
]