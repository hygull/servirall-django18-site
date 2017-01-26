from django.shortcuts import render,redirect
from django.conf import settings
from .forms import SignUpForm,LoginForm
from .models import Post
from django.core.mail import send_mail
# Create your views here.
def home(request):
	title="HyGo"
	# logout=""
	# login="Login"
	# login_url="/admin/login/?next=/admin/"
	# logout_url="#"
	# login_url_link_as_list="<li><a id='login' href='/admin/login/?next=/admin/'>Login</a></li>"
	login_url_link_as_list="<li><a id='login' href='/accounts/login/'>Login</a></li>"
	logout_url_link_as_list=""
	# username="Dear visitor"    """............Won't affect"""
	username="Dear!!!"

	if request.method=="POST":
		print request.POST

	if request.user.is_authenticated():
		username=request.user
		login_url_link_as_list=""
		logout_url_link_as_list="<li><a id='login' href='/admin/logout/'>Logout</a></li>"
	else:
		request.user="Dear visitor"
	context={"title":title,"username":username,"login_url_link_as_list":login_url_link_as_list,"logout_url_link_as_list":logout_url_link_as_list}
	return render(request,"home.html",context)

def login(request):#Model Form
	print "Request Method :",request.POST

	form=SignUpForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		print "Enetered   Email : ",instance.email
		print "Entered Username : ",instance.username
		print "Other way to get entered email : ",form.cleaned_data.get("email")
		print "Redirecting ... "
		return redirect("/submit/")
	else:
		print "Form is not valid..."
	print "Ok...."
	return render(request,"login.html",{"form":form}) 

def success(request):
	print "Succesfully logged in..."
	return render(request,"success.html",{}) 

def error(request):
	print "You didn't entered proper data..."
	return render(request,"error.html",{}) 

def login2(request): #Simple ordinary form
	form=LoginForm(request.POST or None)
	if form.is_valid():
		print form.cleaned_data
		for k,v in form.cleaned_data.iteritems(): ##request.cleaned_data will not work here...WSGIRequest' object has no attribute 'cleaned_data'
			print k," => ",v
		to_email=form.cleaned_data.get("email")#request.cleaned_data will not work here...WSGIRequest' object has no attribute 'cleaned_data'
		print "Sending an email to ",to_email
		send_mail("Simple Description",
			"A simple message",
			settings.EMAIL_HOST_USER,
			[to_email,],
			html_message="""
			<h1 style='color:blue;'>Hello Golangers</h1>
			""",
			fail_silently=True,
			)
		print "email sent..."
		return redirect("/submit/")
	return render(request,"login2.html",{"form":form}) 
	
def blogs(request):
	title="Blog"
	login_url_link_as_list="<li><a id='login' href='/accounts/login/'>Login</a></li>"
	logout_url_link_as_list=""

	if request.user.is_authenticated():
		login_url_link_as_list=""
		logout_url_link_as_list="<li><a id='login' href='/admin/logout/'>Logout</a></li>"

	context={"title":title,"login_url_link_as_list":login_url_link_as_list,"logout_url_link_as_list":logout_url_link_as_list}
	
	return render(request,"blogs.html",context)

def posts(request):
	title="Posts"
	login_url_link_as_list="<li><a id='login' href='/accounts/login/'>Login</a></li>"
	logout_url_link_as_list=""
<<<<<<< HEAD
	posts=""
	if request.user.is_authenticated():
		login_url_link_as_list=""
		logout_url_link_as_list="<li><a id='login' href='/admin/logout/'>Logout</a></li>"
		posts=Post.objects.all()
	else:
		posts+="No posts found"
	context={"title":title,"login_url_link_as_list":login_url_link_as_list,"logout_url_link_as_list":logout_url_link_as_list,"posts":posts}
=======

	if request.user.is_authenticated():
		login_url_link_as_list=""
		logout_url_link_as_list="<li><a id='login' href='/admin/logout/'>Logout</a></li>"

	context={"title":title,"login_url_link_as_list":login_url_link_as_list,"logout_url_link_as_list":logout_url_link_as_list}
>>>>>>> eacbbcddd1e503498e98c3633fa98121fd3fa120
	
	return render(request,"posts.html",context)

def aboutus(request):
	title="Blog"
	login_url_link_as_list="<li><a id='login' href='/accounts/login/'>Login</a></li>"
	logout_url_link_as_list=""

	if request.user.is_authenticated():
		login_url_link_as_list=""
		logout_url_link_as_list="<li><a id='login' href='/admin/logout/'>Logout</a></li>"
	context={"title":title,"login_url_link_as_list":login_url_link_as_list,"logout_url_link_as_list":logout_url_link_as_list}
	
	return render(request,"aboutus.html",context)

def dtl_home(request):
	return render(request,"dtl_home.html",{})

def dtl_aboutus(request):
	return render(request,"dtl_aboutus.html")

def dtl_contact(request):
	return render(request,"dtl_contact.html")