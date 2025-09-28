from .views import *
from django.urls import path
app_name = 'accounts'
urlpatterns = [
    path('auth/', auth_view, name='auth'),
    path('logout/', logout_view, name='logout'),
    path('delete-account/', delete_account, name='delete_account'),
]