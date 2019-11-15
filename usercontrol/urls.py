from django.urls import path
from .views import *


app_name = 'usercontrol'
urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('success/', register_success_view, name='success'),
    path('logout/', logout_view, name='logout')

]
