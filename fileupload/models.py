# encoding: utf-8
import os
from project.settings import THUMBNAIL_SIZE, AUTH_USER_MODEL, DELETE_MEDIA_FILES
from PIL import Image
from django.db import models
from django.utils import timezone
from io import BytesIO
from django.core.files.base import ContentFile


def file_name_extension(filename):
    name, extension = os.path.splitext(filename)
    return name.lower(), extension.lower()


def make_thumbnail(instance, size=None):
    image = Image.open(instance.file)
    if size and isinstance(size, tuple) and isinstance(size[0], int) and isinstance(size[1], int):
        thumb_size = size
    else:
        thumb_size = THUMBNAIL_SIZE
    image.thumbnail(thumb_size, Image.ANTIALIAS)
    thumb_name, thumb_extension = file_name_extension(instance.file.name)
    thumb_filename = thumb_name + '_thumb' + thumb_extension
    if thumb_extension in ['.jpg', '.jpeg']:
        FTYPE = 'JPEG'
    elif thumb_extension == '.gif':
        FTYPE = 'GIF'
    elif thumb_extension == '.png':
        FTYPE = 'PNG'
    else:
        return False  # Unrecognized file type
    # Save thumbnail to in-memory file as StringIO
    temp_thumb = BytesIO()
    image.save(temp_thumb, FTYPE)
    temp_thumb.seek(0)
    # set save=False, otherwise it will run in an infinite loop
    instance.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
    temp_thumb.close()
    return True


def upload_to(instance, filename):
    name, extension = file_name_extension(filename)
    instance.slug = name[:20]
    filename = '{}{}'.format(name[:20], extension)
    instance.file.name = filename
    if not make_thumbnail(instance):
        raise Exception('Could not create thumbnail - is the file type valid?')
    return 'pictures/{}/{}'.format(timezone.now().strftime('%Y/%m/%d'), filename)


class Picture(models.Model):
    file = models.ImageField(upload_to=upload_to, blank=True)
    slug = models.SlugField(max_length=20, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/%Y/%m/%d', blank=True)
    user = models.ForeignKey(AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    deleted = models.BooleanField(default=False)
    show = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

    def get_absolute_url(self):
        return ('upload-new', )

    def delete(self, *args, **kwargs):
        """delete -- Remove to leave file."""
        self.file.delete(DELETE_MEDIA_FILES)
        self.thumbnail.delete(DELETE_MEDIA_FILES)
        super(Picture, self).delete(*args, **kwargs)
