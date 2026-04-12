import cloudinary.uploader
from cloudinary_storage.storage import MediaCloudinaryStorage


class VideoCloudinaryStorage(MediaCloudinaryStorage):
    """Custom storage for video files - uses resource_type='video'"""

    def _upload(self, name, content):
        options = {
            'use_filename': True,
            'resource_type': 'video',
            'folder': 'media/Trailers',
            'tags': 'media',
        }
        return cloudinary.uploader.upload(content, **options)
