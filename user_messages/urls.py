from django.urls import path
from user_messages import views


urlpatterns = [
	path('user_messages/', views.user_messages, name='user_messages'),
	path('api/edit_message/', views.edit_message),
]
