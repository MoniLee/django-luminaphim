# urls.py - File URL chính của toàn bộ dự án LuminaPhim
# Tập hợp tất cả URL từ các ứng dụng con

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = [
    # URL của ứng dụng Home (trang chủ, phim, phim bộ, thể loại...)
    path('', include('Home.urls')),

    # URL của ứng dụng users (đăng nhập, đăng ký, profile)
    path('profile/', include('users.urls')),

    # URL của REST API (dùng cho các request từ frontend hoặc mobile)
    path('api/', include('api.urls')),

    # URL trang quản trị Django Admin
    path('admin/', admin.site.urls),
]

# Thêm URL cho static files (CSS, JS, ảnh tĩnh)
urlpatterns += staticfiles_urlpatterns()

# Chỉ serve media files qua Django khi chạy local (không có Cloudinary)
# Khi deploy lên Render, Cloudinary sẽ tự handle media files
if not settings.CLOUDINARY_URL:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
