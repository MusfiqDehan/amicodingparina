from django.contrib import admin
from django.urls import path, include
from api.models import InputResource
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

input_resource = InputResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('khoj.urls')),
    path('api/v1/', include(input_resource.urls)),
]

urlpatterns += staticfiles_urlpatterns()
handler404 = 'khoj.views.page_not_found_view'
