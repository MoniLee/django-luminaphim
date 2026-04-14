# urls.py - Định nghĩa các URL pattern cho ứng dụng Home
# File này được include vào LuminaPhim/urls.py (file URL chính)

from django.urls import path
from .views import *  # Import tất cả view functions

urlpatterns = [
    # Trang chủ - hiển thị danh sách phim
    path('', HomePage, name='Home'),

    # Trang chi tiết phim lẻ - pk là UUID của phim
    path('movie/<str:pk>/', SingleMoviePage, name='single-movie'),

    # Trang chi tiết phim bộ - pk là UUID của phim bộ
    path('serial/<str:pk>/', SingleSerialPage, name='single-serial'),

    # Trang danh sách phim theo thể loại - pk là UUID của thể loại
    path('genre/<str:pk>/', SingleGenrePage, name='single-genre'),

    # Trang danh sách phim theo đạo diễn - pk là UUID của đạo diễn
    path('director/<str:pk>/', SingleDirectorPage, name='single-director'),

    # Trang phản hồi / góp ý
    path('feedback/', FeedbackPage, name='feedback'),

    # Trang thông báo gửi phản hồi thành công
    path('feedback-success/', FeedbackSuccess, name='feedback-success'),

    # Trang giới thiệu về LuminaPhim
    path('about/', AboutPage, name='about'),
]
