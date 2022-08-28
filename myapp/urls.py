
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from . import views

#..............

urlpatterns=[
    
    re_path('^$',views.welcome,name = 'index'),
    re_path('projects',views.allprojects,name='projects'),
    re_path(r'^singleproject/(?P<project_id>\d+)?$',views.project, name='singleproject'), 

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)