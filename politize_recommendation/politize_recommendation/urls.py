from django.conf.urls import include
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('v1/', include(('v1.urls', 'v1')))
]
