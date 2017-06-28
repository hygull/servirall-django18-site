from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

# Create your models here.
class SignUp(models.Model):
	username = models.CharField(max_length=20,null=True,blank=True)
	email = models.EmailField(max_length=30)
	created_at = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated_at = models.DateTimeField(auto_now_add=False,auto_now=True)

	def __unicode__(self):  
		return self.username


class Post(models.Model):
	title = models.CharField(max_length=150,null=False,blank=False)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated_at = models.DateTimeField(auto_now_add=False,auto_now=True)

	def __unicode__(self):
		return self.title

	def get_absolute_path(self):
		return "http://rishikesh67.pythonaywhere.com/posts/%d"%(self.id)



class Video(models.Model):
	title = models.CharField(max_length=150,null=False,blank=False)
	url = models.TextField()

	def __unicode__(self):
		return self.title

class VideoVirtualReality(models.Model):
	title = models.CharField(max_length=150,null=False,blank=False)
	url = models.CharField(max_length=150,null=False,blank=False)

	def __unicode__(self):
		return self.title

class Markdown(models.Model):
	name = models.CharField(max_length=100, blank=False)
	markdown_text = models.TextField()

	def __unicode__(self):
		return self.name

class Product(models.Model):
	""" Product model """
	title = models.CharField(max_length=500, blank=False)
	image = models.TextField(blank=False)
	price = models.FloatField(blank=False)
	stock_status = models.IntegerField(validators=[MaxValueValidator(1), MinValueValidator(0)], blank=False)
	target_url = models.TextField(blank=False)
	merchant = models.CharField(max_length=5,blank=False)

	def __unicode__(self):
		return self.title

class Click(models.Model):
	clicks = models.BigIntegerField()


def validate_discount(value):
	if value < 0.0:
		raise ValidationError("discount should be positive")

class FishImage(models.Model):
	""" A class that defines the structure of User object """
	COLOR_CHOICES = (
	    (1, 'Type1'),
	    (2, 'Type2'),
	    (3, 'Type3'),
	    (4, 'Type4'),
	    (5, 'Type5'),
	    (6, 'Type6'),
	    (7, "Other"),
	)

	flesh_name = models.CharField(max_length=50, blank=False)	#Required
	flesh_type = models.CharField(max_length=50, blank=False)
	flesh_pic = models.ImageField(default="https://en.wikipedia.org/wiki/List_of_types_of_seafood#/media/File:Squilla_mantis_(l%27Ametlla)_brighter_and_quality.jpg", max_length=200)
	flesh_type = models.IntegerField(choices=COLOR_CHOICES, default='Type0', blank=True)
	price = models.FloatField(blank=False)
	discount = models.IntegerField(validators=[validate_discount], default=0, blank=True)

	def __unicode__(self):
		return self.flesh_name