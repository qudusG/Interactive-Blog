from django.db import models
from django.utils import timezone
import datetime

status = ((0,'Draft'),(1,'Published'))

class Post(models.Model):
	title = models.CharField(max_length = 200)
	author = models.CharField(max_length = 40)
	content = models.TextField()
	date = models.DateTimeField('Publication Date')
	last_modified = models.DateTimeField('Last Modified',auto_now = True)
	status = models.IntegerField(choices=status, default=0)
	
	def pub_date(self):
		self.date = timezone.now()

	def __str__(self):
 		return self.title

class Comment(models.Model):
	author = models.CharField(max_length = 40)
	reply = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey('Post', on_delete=models.CASCADE)
	active = models.BooleanField(default=False)

	class Meta:
		ordering = ['-date']