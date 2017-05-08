from django.shortcuts import render,redirect
from django.conf import settings
from .forms import SignUpForm,LoginForm,PostForm,VideoForm
from .models import Post,Video,Markdown
from django.core.mail import send_mail
# Create your views here.

def rscript(request):
	markdown_obj = Markdown.objects.get(name="rscript")
	return render(request , "rscript.html", {"markdown_text":markdown_obj.markdown_text}) 

def supermarket(request):
	return render(request , "supermarket.html", {}) 

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
	print "HOME PATH: ",request.get_full_path();
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
	posts=""
	posts_message=""
	if request.user.is_authenticated():
		login_url_link_as_list=""
		logout_url_link_as_list="<li><a id='login' href='/admin/logout/'>Logout</a></li>"
		posts=Post.objects.all()
		print "The posts available are as follows:\n",posts
	else:
		posts_message="""<h3 style='color:gray;text-align:center;'> No posts found</h3><h4 style='text-align:center;'><hr>Please <span style='color:navy;'><a href='/accounts/login/'>login</a></span> to the see protected posts</h4><hr><h5 style='color:blue;text-align:center;'>Username:  <span style='color:orange;'>root</span><br>Password: <span style='color:orange;'>admin@321</span></h5><hr>
		<center><img src='http://theworldly.co.uk/wp-content/uploads/2017/01/tech-wowcity.jpg' width='90%'><hr>
		<img src='http://www.robertwmills.com/wp-content/uploads/2016/03/healthcare-technology-8-04-2015.jpg' width='90%'> <hr>
		<img src='http://i.huffpost.com/gen/1980282/images/o-BUSINESS-TECHNOLOGY-facebook.jpg' width='90%'><hr>

		</center>
		"""
	context={"title":title,"login_url_link_as_list":login_url_link_as_list,"logout_url_link_as_list":logout_url_link_as_list,"posts":posts,"posts_message":posts_message}

	if request.user.is_authenticated():
		login_url_link_as_list=""
		logout_url_link_as_list="<li><a id='login' href='/admin/logout/'>Logout</a></li>"

	context={"title":title,"login_url_link_as_list":login_url_link_as_list,"logout_url_link_as_list":logout_url_link_as_list,"posts":posts,"posts_message":posts_message}
	
	return render(request,"posts.html",context)

def posts_create(request):
	form=PostForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=True)
		print "Title: ",instance.title
		print "Description: ",instance.description
		print "post created..."
		return redirect("/created/")
	return render(request,"posts_create.html",{"form":form}) 

def posts_created(request):
	return render(request,"posts_created.html",{}) 


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
	return render(request,"dtl_aboutus.html",{})

def dtl_contact(request):
	return render(request,"dtl_contact.html")


def posted_videos(request):
	videos=Video.objects.all()[::-1]
	for video in videos:
		print "1...",video.url
		video.url="https://www.youtube.com/embed/"+video.url
		print "2...",video.url
	print videos
	return render(request,"posted_videos.html",{"videos":videos})

def posts_videos_create(request):
	form=VideoForm(request.POST or None)
	try:
		if form.is_valid():
			instance=form.save()
			url=instance.url
			l=url.split("/")
			instance.url=l[3]
			instance=form.save(commit=True)
			print "Title: ",instance.title
			print "URL: ",instance.url
			print "post created..."
			return redirect("/posts/videos/")
	except:
		print "unknown error...<...youtube url or title ...>"
		return redirect("/url_error_message/")
	return render(request,"posts_videos_create.html",{"form":form}) 
# def page_not_found(request):
# 	return render(request,"404.html")
def url_error_message(request):
	print "You didn't enter proper youtube url...https://youtu.be/YB8oOwOra0Q"
	return render(request,"url_error_message.html",{}) 


#Error pages
from django.shortcuts import render_to_response
from django.template import RequestContext


# def handler404(request):
def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

def profile_info(request,extra):
	profile=request.get_full_path()
	l=profile.split("+")
	print l,"\n\n"
	print "Path : ",request.get_full_path(),"\n";
	print "Extra : ",extra
	return render(request,"profile_info.html",{"profile_email":request.get_full_path(),"extra":extra,"id":l[1],"name":l[2].replace("%20"," "),"image":l[3],"email":l[4]})


def login_with_google(request):
	if "servirall_username" in request.COOKIES :
		return redirect("/home/") 
	else:
		return redirect("/login2/")