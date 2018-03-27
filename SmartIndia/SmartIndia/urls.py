
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('fir/', include('fir.urls')),
    path('response/', include('response.urls')),
    path('police/', include('police.urls')),
]
