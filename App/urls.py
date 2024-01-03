
from django.urls import path
from App.views import home, login_view, register, profile, edit_profile, delete_profile
from .views import message_list, send_message


urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile/edit/', edit_profile, name='edit_profile'),
    path('accounts/profile/delete/', delete_profile, name='delete_profile'),
    path('messages/', message_list, name='message_list'),
    path('messages/send/<int:recipient_id>/', send_message, name='send_message'),
    path('messages/send/', send_message, name='send_message'),
    
]

