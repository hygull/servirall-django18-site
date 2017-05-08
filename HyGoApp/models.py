from django.db import models

# Create your models here.
class SignUp(models.Model):
	username=models.CharField(max_length=20,null=True,blank=True)
	email=models.EmailField(max_length=30)
	created_at=models.DateTimeField(auto_now_add=True,auto_now=False)
	updated_at=models.DateTimeField(auto_now_add=False,auto_now=True)

	def __unicode__(self):  
		return self.username


class Post(models.Model):
	title=models.CharField(max_length=150,null=False,blank=False)
	description=models.TextField()
	created_at=models.DateTimeField(auto_now_add=True,auto_now=False)
	updated_at=models.DateTimeField(auto_now_add=False,auto_now=True)

	def __unicode__(self):
		return self.title

	def get_absolute_path(self):
		return "http://rishikesh67.pythonaywhere.com/posts/%d"%(self.id)

class Video(models.Model):
	title=models.CharField(max_length=150,null=False,blank=False)
	url=models.TextField()

	def __unicode__(self):
		return self.title

class Markdown(models.Model):
	name = models.CharField(max_length=100, blank=False)
	markdown_text = models.TextField()

	def __unicode__(self):
		return self.name