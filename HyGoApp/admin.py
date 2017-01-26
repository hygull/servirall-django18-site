from django.contrib import admin

from .models import SignUp, Post
from .forms import SignUpForm
#Register your models here.
class SignUpAdmin(admin.ModelAdmin):
	list_display=["__unicode__","email","created_at","updated_at"]
	class Meta:
		model=SignUp
	form = SignUpForm

class PostAdmin(admin.ModelAdmin):
	list_display=["title","description"]
	class Meta:
		model=Post

admin.site.register(SignUp,SignUpAdmin)
admin.site.register(Post,PostAdmin)
#admin.site.register(SignUp)