from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = [
    path('', include('Home.urls')),
    path('profile/', include('users.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()

# Only serve media locally (Cloudinary handles it in production)
if not settings.CLOUDINARY_URL:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)