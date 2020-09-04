from django.shortcuts import render
from user_messages.models import UserMessages
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@login_required(login_url='login')
def user_messages(request):
	all_messages = UserMessages.objects.all()
	return render(request, 'user_messages/messages.html', {'all_msgs': all_messages})


@api_view(['POST'])
def edit_message(request):
	msg_id = request.data.get('msg_id', None)
	msg_action = request.data.get('action', None)
	user_msg = UserMessages.objects.get(msg_id=msg_id)
	if request.method == 'POST':
		if msg_action == 'read':
			user_msg.was_read = True
			user_msg.save()
		elif msg_action == 'unread':
			user_msg.was_read = False
			user_msg.save()
		return Response({})
	return Response({})
