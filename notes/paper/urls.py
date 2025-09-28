from .views import *
from django.urls import path
from . import views

app_name = 'paper'

urlpatterns = [
    path('home/', home, name='home'),
    path('create_note/', create_note, name='create_note'),
    path('delete_note/<int:note_id>/', delete_note, name='delete_note'),
    path('view_note/<int:note_id>/', view_note, name='view_note'),
    path('note/<int:note_id>/edit/', views.update_note, name='update_note'),
    path('settings/', settings, name='settings'),
]