from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib import admin 
from django.urls import path,include
from .views import UserDetailView

urlpatterns = [ 

path('admin/', admin.site.urls),
path('ckeditor5/', include('django_ckeditor_5.urls')),
path('api/v1/', include('djoser.urls')), 
path('api/v1/', include('djoser.urls.authtoken')), 

path('api/v1/user/', UserDetailView.as_view(), name='user-detail'),
path('api/v1/', include('student.urls')), 
path('api/v1/', include('course.urls')), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

