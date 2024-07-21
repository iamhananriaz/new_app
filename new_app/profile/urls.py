from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('profile/', profile, name='profile'),
]