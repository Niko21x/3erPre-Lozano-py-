
from django.urls import path
from App.views import home, login_view , signup, profile

urlpatterns = [
    path('', home, name='home'),
     path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('profile/', profile , name='profile'),

]
