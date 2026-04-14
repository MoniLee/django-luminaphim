# forms.py - Định nghĩa các form nhập liệu cho ứng dụng Home
# Dùng ModelForm để tự động tạo form từ model

from django.db import models
from .models import comments, comments_serial, Feedback  # Import các model cần tạo form
from django.forms import ModelForm, widgets


class CommentsForm(ModelForm):
    """
    Form bình luận cho trang phim lẻ
    Chỉ hiển thị 2 trường: tên người dùng và nội dung bình luận
    """
    class Meta:
        model = comments          # Dựa trên model comments
        fields = ['name', 'body'] # Chỉ hiển thị 2 trường này

        label = {
            'name': 'Họ Và Tên',
            'body': 'Thêm bình luận'
        }

    def __init__(self, *args, **kwargs):
        super(CommentsForm, self).__init__(*args, **kwargs)
        # Thêm class CSS 'form_title' cho tất cả các input để style đồng nhất
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form_title'})


class CommentsFormSerial(ModelForm):
    """
    Form bình luận cho trang phim bộ
    Tương tự CommentsForm nhưng dùng model comments_serial
    """
    class Meta:
        model = comments_serial
        fields = ['name', 'body']

        label = {
            'name': 'Họ Và Tên',
            'body': 'Thêm bình luận'
        }

    def __init__(self, *args, **kwargs):
        super(CommentsFormSerial, self).__init__(*args, **kwargs)
        # Thêm class CSS cho các input
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form_title'})


class FeedbackForm(ModelForm):
    """
    Form phản hồi / góp ý từ người dùng
    Gồm 3 trường: tên, email và nội dung phản hồi
    """
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']

        label = {
            'name': 'Họ và Tên',
            'email': 'Email',
            'message': 'Nội dung phản hồi'
        }

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        # Thêm class CSS cho các input
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form_title'})
