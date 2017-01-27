# from django.conf.urls import include, url,handler404

# handler404='views.page_not_found'

# urlpatterns = [
        
# ]			

from django.conf.urls import handler404

handler404='views.page_not_found'		

handler500='views.server_error'	