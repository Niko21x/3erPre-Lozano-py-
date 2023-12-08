
from django.contrib import admin
from django.urls import path, include
from App.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('App/', include('App.urls')),
     path('', home , name='inicio')
]
