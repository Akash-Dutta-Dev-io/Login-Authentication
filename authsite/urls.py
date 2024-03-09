from django.contrib import admin
from django.urls import path, include
from core.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='login'), 
    path('register/', include('core.urls')),  
]
