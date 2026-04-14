# models.py - Định nghĩa cấu trúc database của ứng dụng Home
# Mỗi class tương ứng với một bảng trong database

from django.db import models
import uuid
from django.conf import settings


def get_trailer_storage():
    """
    Hàm trả về storage phù hợp cho file trailer video.
    - Nếu có CLOUDINARY_URL (môi trường production): dùng VideoCloudinaryStorage để upload lên Cloudinary
    - Nếu không có (môi trường local): dùng FileSystemStorage để lưu trên ổ đĩa
    """
    if settings.CLOUDINARY_URL:
        from Home.storage import VideoCloudinaryStorage
        return VideoCloudinaryStorage()
    from django.core.files.storage import FileSystemStorage
    return FileSystemStorage()


# ==================== MODEL PHIM ====================
class HomePageModel(models.Model):
    """Model đại diện cho một bộ phim trong hệ thống"""

    title = models.CharField(max_length=200)                          # Tên phim
    director = models.ForeignKey('Director', on_delete=models.CASCADE, default=None)  # Đạo diễn (khóa ngoại)
    release_date = models.CharField(max_length=70, default='None')    # Năm phát hành
    short_intro = models.TextField(max_length=700)                    # Giới thiệu ngắn
    IMDb_RATING = models.CharField(max_length=50, default=None)       # Điểm IMDb
    genre = models.ManyToManyField('Genre')                           # Thể loại (nhiều-nhiều)
    poster = models.ImageField(upload_to='Posters/')                  # Ảnh poster chính
    movie_page_poster = models.ImageField(upload_to='Posters/MoviePage/', null=True, blank=True)  # Ảnh banner trang phim
    summary = models.TextField(max_length=1600)                       # Tóm tắt nội dung
    trailer_file = models.FileField(upload_to='Trailers/', null=True, blank=True, storage=get_trailer_storage)  # File video trailer
    download_link_1080 = models.CharField(max_length=650, null=True, blank=True)  # Link tải 1080p
    download_link_720 = models.CharField(max_length=650, null=True, blank=True)   # Link tải 720p
    download_link_480 = models.CharField(max_length=650, null=True, blank=True)   # Link tải 480p
    page_view = models.IntegerField(default=1)                        # Số lượt xem
    created = models.DateTimeField(auto_now_add=True)                 # Thời gian tạo (tự động)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)  # ID duy nhất dạng UUID

    def __str__(self):
        return self.title  # Hiển thị tên phim trong admin

    class Meta:
        ordering = ['-created']  # Sắp xếp mới nhất lên đầu


# ==================== MODEL PHIM BỘ ====================
class Serial(models.Model):
    """Model đại diện cho một bộ phim bộ (series)"""

    Serial_name = models.CharField(max_length=200)                    # Tên phim bộ
    director = models.ForeignKey('Director', on_delete=models.CASCADE, default=None)  # Đạo diễn
    release_date = models.CharField(max_length=70, default='None')    # Năm phát hành
    short_intro = models.TextField(max_length=700)                    # Giới thiệu ngắn
    IMDb_RATING = models.CharField(max_length=50, default=None)       # Điểm IMDb
    genre = models.ManyToManyField('Genre')                           # Thể loại
    poster = models.ImageField(upload_to='Posters/')                  # Ảnh poster
    seriel_page_poster = models.ImageField(upload_to='Posters/SerialPage/', null=True, blank=True)  # Ảnh banner
    summary = models.TextField(max_length=1600)                       # Tóm tắt
    trailer_file = models.FileField(upload_to='Trailers/', null=True, blank=True, storage=get_trailer_storage)  # File trailer
    page_view = models.IntegerField(default=1)                        # Lượt xem
    seasons = models.ManyToManyField('Season', default=None)          # Các mùa (nhiều-nhiều)
    episodes = models.ManyToManyField('Episode', default=None)        # Các tập (nhiều-nhiều)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.Serial_name

    class Meta:
        ordering = ['-created']


# ==================== MODEL MÙA ====================
class Season(models.Model):
    """Model đại diện cho một mùa của phim bộ"""

    season_name = models.CharField(max_length=50, default='S01 - Serial Name')  # Tên mùa (vd: S01 - Breaking Bad)
    Episodes = models.ManyToManyField('Episode', default=None)        # Các tập trong mùa
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.season_name


# ==================== MODEL TẬP PHIM ====================
class Episode(models.Model):
    """Model đại diện cho một tập phim trong phim bộ"""

    chose_season = models.ForeignKey('Season', on_delete=models.CASCADE, default=None, null=True, blank=True)  # Thuộc mùa nào
    episode_number = models.CharField(max_length=50, default='E01 - Serial Name')  # Số tập (vd: E01 - Pilot)
    download_link1080 = models.CharField(max_length=650, null=True, blank=True)   # Link tải 1080p
    download_link720 = models.CharField(max_length=650, null=True, blank=True)    # Link tải 720p
    download_link480 = models.CharField(max_length=650, null=True, blank=True)    # Link tải 480p
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.episode_number


# ==================== MODEL THỂ LOẠI ====================
class Genre(models.Model):
    """Model đại diện cho thể loại phim (Action, Drama, ...)"""

    name = models.CharField(max_length=200)       # Tên thể loại
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


# ==================== MODEL ĐẠO DIỄN ====================
class Director(models.Model):
    """Model đại diện cho đạo diễn"""

    name = models.CharField(max_length=200)       # Tên đạo diễn
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


# ==================== MODEL BÌNH LUẬN PHIM ====================
class comments(models.Model):
    """Model lưu bình luận của người dùng cho phim lẻ"""

    movie_page = models.ForeignKey(HomePageModel, on_delete=models.CASCADE, null=True, related_name='comments')  # Phim được bình luận
    name = models.CharField(max_length=200, default='Guest')          # Tên người bình luận
    body = models.TextField(max_length=650, null=True, blank=True)    # Nội dung bình luận
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


# ==================== MODEL BÌNH LUẬN PHIM BỘ ====================
class comments_serial(models.Model):
    """Model lưu bình luận của người dùng cho phim bộ"""

    serial_page = models.ForeignKey(Serial, on_delete=models.CASCADE, null=True, related_name='comments_serial')  # Phim bộ được bình luận
    name = models.CharField(max_length=200, default='Guest')
    body = models.TextField(max_length=650, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


# ==================== MODEL PHẢN HỒI ====================
class Feedback(models.Model):
    """Model lưu phản hồi/góp ý từ người dùng"""

    name = models.CharField(max_length=200)       # Tên người gửi
    email = models.EmailField()                   # Email liên hệ
    message = models.TextField(max_length=2000)   # Nội dung phản hồi
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        ordering = ['-created']
