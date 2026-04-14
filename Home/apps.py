# apps.py - Cấu hình ứng dụng Home
# Django dùng file này để nhận diện và cấu hình app

from django.apps import AppConfig


class HomeConfig(AppConfig):
    # Kiểu primary key mặc định cho các model không khai báo pk
    default_auto_field = 'django.db.models.BigAutoField'

    # Tên ứng dụng - phải khớp với tên folder và INSTALLED_APPS trong settings.py
    name = 'Home'
