from django.contrib import admin
from django.urls import path, include
from api.models import InputResource

input_resource = InputResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('khoj.urls')),
    path('api/v1/', include(input_resource.urls)),
]
