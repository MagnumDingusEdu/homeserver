from django.urls import path
from .views import *


app_name = 'landing'
urlpatterns = [
    path('', landing_page_view,  name='index'),
    path('applications/', rickroll_view, name='gotcha'),
    path('cloud/', rickroll_view, name='gotcha2'),



]
