from django.conf.urls import include, url,handler404
from django.contrib import admin
from django.conf import settings #Added
from django.conf.urls.static import static #Added 

handler404='HyGoApp.views.page_not_found'

urlpatterns = [
    # Examples:
    url(r'^$', 'HyGoApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$', 'HyGoApp.views.login', name='login'),
    url(r'^login2/$', 'HyGoApp.views.login2', name='login2'),
    url(r'^submit/$', 'HyGoApp.views.success', name='success'),
    url(r'^error/$', 'HyGoApp.views.error', name='error'),
    url(r'^admin/', include(admin.site.urls)),

    url(r"^blogs/$","HyGoApp.views.blogs",name="blogs"),
    url(r"^aboutus/$","HyGoApp.views.aboutus",name="aboutus"),
    url(r"^posts/$","HyGoApp.views.posts",name="posts"),
    url(r"^posts/create/$","HyGoApp.views.posts_create",name="posts_create"),
    url(r"^created/$","HyGoApp.views.posts_created",name="servirall_aboutus"),

    url(r"^dtl_home/$","HyGoApp.views.dtl_home",name="dtl_home"),
    url(r"^dtl_home/aboutus/$","HyGoApp.views.dtl_aboutus",name="servirall_aboutus"),
    #url(r"^dtl_base/contact/$","HyGoApp.views.dtl_contact",name="servirall_contact"),

    url(r'^accounts/', include('registration.backends.default.urls')), #dajngo-registration-redux
]	#+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)		

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)	
