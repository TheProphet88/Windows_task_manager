from django.contrib import admin
from django.urls import include, path


app_name = 'process'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('process.urls')),
    
]
