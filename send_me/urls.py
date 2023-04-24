from django.urls import path
from.import views


urlpatterns =[
    path('',views.index, name='send_me-index'),
    path('sent/', views.sent, name='send_me-sent'),
    path('recieved/', views.recieved, name='send_me-recieved'),
    path('branches/', views.branches, name='send_me-branches'),
]