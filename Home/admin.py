# admin.py - Đăng ký các model để quản lý qua Django Admin
# Sau khi đăng ký, admin có thể thêm/sửa/xóa dữ liệu tại /admin/

from django.contrib import admin
from .models import *  # Import tất cả models từ models.py

# Đăng ký model phim lẻ
admin.site.register(HomePageModel)

# Đăng ký model thể loại
admin.site.register(Genre)

# Đăng ký model đạo diễn
admin.site.register(Director)

# Đăng ký model phim bộ
admin.site.register(Serial)

# Đăng ký model mùa phim
admin.site.register(Season)

# Đăng ký model tập phim
admin.site.register(Episode)

# Đăng ký model bình luận phim lẻ
admin.site.register(comments)

# Đăng ký model bình luận phim bộ
admin.site.register(comments_serial)

# Đăng ký model phản hồi
admin.site.register(Feedback)
