from django.db import models

# Create your models here.

class UserMessages(models.Model):
	msg_id = models.AutoField(primary_key=True)
	msg_title = models.CharField(max_length=50)
	msg_content = models.TextField(max_length=200)
	was_read = models.BooleanField(default=False)


