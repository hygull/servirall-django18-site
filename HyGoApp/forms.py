from django import forms

from .models import SignUp,Post,Video,VideoVirtualReality

import re

class SignUpForm(forms.ModelForm):
	class Meta:
		model=SignUp
		# form = SignUp
		fields=["username","email"] #Some fields can be excluded

	def clean_username(self):
		signup_dict=self.cleaned_data
		print "SignUp Details : ",signup_dict
		username=signup_dict["username"]
		lst=re.findall(r"^([A-Z]{1})([a-z]{2,19})$",username)
		print "Matched : ",lst
		if not len(lst)==1:
			print "Not matched..."
			raise forms.ValidationError("First letter of username should be in capital followed by 2 to 19 small case letters")
		return username

	def clean_email(self):
		signup_dict = self.cleaned_data
		print "SignUp details : ",signup_dict
		email = signup_dict["email"]
		lst = re.findall(r"^[a-z]{3,30}@gmail.com$",email)
		print "Matched : ",lst
		if not len(lst) == 1:
			raise forms.ValidationError("Only gmail is allowed. Email should be in the form eg. hem@gmail.com & golang@gmail.com etc.Maximum length should be 30")
		return email #In absence of this line => This field can't be null

class LoginForm(forms.Form):
	username = forms.CharField(max_length=20)
	email = forms.EmailField(max_length=30)

	def clean_username(self):
		signup_dict=self.cleaned_data
		print "Login Details : ",signup_dict
		username = signup_dict["username"]
		lst = re.findall(r"^([A-Z]{1})([a-z]{2,19})$",username)
		print "Matched : ",lst
		if not len(lst) == 1:
			print "Not matched..."
			raise forms.ValidationError("First letter of username should be in capital followed by 2 to 19 small case letters")
		return username

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		# form = SignUp
		fields = ["title","description"] #Some fields can be excluded

	def clean_title(self):
		title = self.cleaned_data["title"]
		print "Cleaning title, got >> ",title
		if len(title) == 0:
			return forms.ValidationError("Title should not be blank")
		return title

	def clean_description(self):
		description = self.cleaned_data["description"]
		print "Cleaning description, got >> ",description
		if len(description) == 0:
			return forms.ValidationError("Descrition should not be blank")
		return description

class VideoForm(forms.ModelForm):
	class Meta:
		model = Video
		# form = SignUp
		fields = ["title","url"] #Some fields can be excluded

		#For placeholders
		widgets = {
			"title":forms.TextInput(attrs={"placeholder":"Enter the title of video from youtube..."}),
			"url":forms.Textarea(attrs={"placeholder":"Paste the video URL from youtube..."})
		}

	def clean_title(self):
		title = self.cleaned_data["title"]
		print "Cleaning title, got >> ",title
		if len(title) == 0:
			raise forms.ValidationError("Title should not be blank")
		return title

	def clean_url(self):
		url=self.cleaned_data["url"]
		print "Cleaning url, got >> ",url
		l=url.split('/')
		if not len(l)==4:
			raise forms.ValidationError("Wrong URL. The url should be like this =>  https://youtu.be/Kg9DGBLHUfw")
		else:
			if not l[0]=="https:" or not  l[1]=="":
				raise forms.ValidationError("Wrong URL. The url should start with => https://. eg https://youtu.be/Kg9DGBLHUfw")
			else:
				if not l[2]=='youtu.be':
					raise forms.ValidationError("Wrong URL, The url should contain => youtu.be. It should be like => https://youtu.be/Kg9DGBLHUfw")
		return url
	# def clean_email(self):
	# 	signup_dict=self.cleaned_data
	# 	print "Login details : ",signup_dict
	# 	email=signup_dict["email"]
	# 	lst=re.findall(r"^[a-z]{3,30}@gmail.com$",email)
	# 	print "Matched : ",lst
	# 	if not len(lst)==1:
	# 		raise forms.ValidationError("Only gmail is allowed. Email should be in the form eg. hem@gmail.com & golang@gmail.com etc.Maximum length should be 30")
	# 	return email #In absence of this line => This field can't be null

class VideoVirtualRealityForm(forms.ModelForm):
	class Meta:
		model = VideoVirtualReality
		# form = SignUp
		fields = ["title","url"] #Some fields can be excluded

		#For placeholders
		widgets = {
			"title":forms.TextInput(attrs={"placeholder":"Enter the title of video from youtube..."}),
			"url":forms.TextInput(attrs={"placeholder":"Paste the video URL from youtube..."})
		}

	def clean_title(self):
		title = self.cleaned_data["title"]
		print "Cleaning title, got >> ",title
		if len(title)==0:
			raise forms.ValidationError("Title should not be blank")
		return title

	def clean_url(self):
		url = self.cleaned_data["url"]
		print "Cleaning url, got >> ",url
		l = url.split('/')
		if not len(l) == 4:
			raise forms.ValidationError("Wrong URL. The url should be like this =>  https://youtu.be/Kg9DGBLHUfw")
		else:
			if not l[0] == "https:" or not  l[1]=="":
				raise forms.ValidationError("Wrong URL. The url should start with => https://. eg https://youtu.be/Kg9DGBLHUfw")
			else:
				if not l[2] == 'youtu.be':
					raise forms.ValidationError("Wrong URL, The url should contain => youtu.be. It should be like => https://youtu.be/Kg9DGBLHUfw")
		return url
