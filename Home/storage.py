# storage.py - Custom storage class cho file video trailer
# Mặc định django-cloudinary-storage upload tất cả file với resource_type='image'
# Class này override để dùng resource_type='video' cho file trailer

import cloudinary.uploader
from cloudinary_storage.storage import MediaCloudinaryStorage  # Base class từ django-cloudinary-storage


class VideoCloudinaryStorage(MediaCloudinaryStorage):
    """
    Custom storage dành riêng cho file video trailer.
    
    Vấn đề gốc: MediaCloudinaryStorage mặc định dùng resource_type='image'
    khiến Cloudinary từ chối file .mp4 với lỗi "Invalid image file".
    
    Giải pháp: Override 2 method:
    - _upload(): chỉ định resource_type='video' khi upload
    - url(): thay /image/upload/ thành /video/upload/ trong URL trả về
    """

    def _upload(self, name, content):
        """
        Override method upload để chỉ định đây là file video.
        Upload vào folder 'media/Trailers' trên Cloudinary.
        """
        options = {
            'use_filename': True,       # Giữ nguyên tên file gốc
            'resource_type': 'video',   # Quan trọng: báo Cloudinary đây là video
            'folder': 'media/Trailers', # Lưu vào folder Trailers
            'tags': 'media',            # Gắn tag để dễ quản lý
        }
        return cloudinary.uploader.upload(content, **options)

    def url(self, name):
        """
        Override method url để sửa đường dẫn từ /image/upload/ thành /video/upload/.
        Cloudinary dùng đường dẫn khác nhau cho ảnh và video.
        """
        url = super().url(name)
        # Thay thế /image/upload/ bằng /video/upload/ để URL hoạt động đúng
        return url.replace('/image/upload/', '/video/upload/')
