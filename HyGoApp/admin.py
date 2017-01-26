from django.contrib import admin

from .models import SignUp
from .forms import SignUpForm
#Register your models here.
class SignUpAdmin(admin.ModelAdmin):
	list_display=["__unicode__","email","created_at","updated_at"]
	class Meta:
		model=SignUp
	form = SignUpForm

admin.site.register(SignUp,SignUpAdmin)

#admin.site.register(SignUp)