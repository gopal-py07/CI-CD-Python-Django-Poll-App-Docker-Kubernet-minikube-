
from django.urls import path
from . import views
app_name = 'polls'
urlpatterns = [
    
    # path('index/', views.index, name='index'),
    path('list/', views.list_poll, name='list'),
    path('<int:p_id>/', views.detailview, name='detail'),
    path('createPoll/', views.create_Poll, name='addPoll'),
    path('<int:p_id>/vote/', views.vote, name='vote'),
    
    
    path('addChoice/<int:p_id>/', views.add_choice, name='addChoice'),
    path('editchoice/<int:choice_id>/', views.choice_edit, name='editchoice'),
    path('choicedelete/<int:choice_id>/',views.choice_delete, name='choicedelete'),
     
    path('edit/<int:p_id>/', views. edit_poll, name='editPoll'),
    path('delete/<int:p_id>/', views.polls_delete, name='deletePoll'),
    
]