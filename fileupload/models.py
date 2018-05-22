# encoding: utf-8
import os
from project.settings import THUMBNAIL_SIZE, AUTH_USER_MODEL
from PIL import Image
from django.db import models
from django.utils.timezone import datetime
from io import BytesIO
from django.core.files.base import ContentFile
from random import randint


def file_name_extension(filename):
    name, extension = os.path.splitext(filename)
    return name.lower(), extension.lower()


def upload_to_picture(instance, filename):
    return '/'.join(['pictures', filename])


def upload_to_thumbnail(instance, filename):
    return '/'.join(['thumbnails', filename])


class Picture(models.Model):
    """This is a small demo using just two fields. The slug field is really not
    necessary, but makes the code simpler. ImageField depends on PIL or
    pillow (where Pillow is easily installable in a virtualenv. If you have
    problems installing pillow, use a more generic FileField instead.

    """
    file = models.ImageField(upload_to=upload_to_picture, blank=True)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    thumbnail = models.ImageField(upload_to=upload_to_thumbnail, blank=True)
    user = models.ForeignKey(AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    deleted = models.BooleanField(default=False)
    show = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

    @models.permalink
    def get_absolute_url(self):
        return ('upload-new',)

    def save(self, *args, **kwargs):
        name, extension = file_name_extension(self.file.name)
        name = '{}_{}'.format(datetime.now().strftime('%d_%m_%Y'), randint(100000, 999999))
        self.file.name = '{}{}'.format(name, extension)
        self.slug = name
        if not self.make_thumbnail():
            # set to a default thumbnail
            raise Exception('Could not create thumbnail - is the file type valid?')
        super(Picture, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """delete -- Remove to leave file."""
        self.file.delete(False)
        self.thumbnail.delete(False)
        super(Picture, self).delete(*args, **kwargs)

    def make_thumbnail(self):
        image = Image.open(self.file)
        image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

        thumb_name, thumb_extension = file_name_extension(self.file.name)

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
        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()

        return True
