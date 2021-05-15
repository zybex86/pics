import uuid
from pathlib import Path

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.utils.translation import gettext_lazy as _


def thumbnail_file_path(instance, filename):
    ext = Path(filename).suffix
    filename = f'{uuid.uuid4()}{ext}'
    return Path('uploads/thumbnail') / filename


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        """Create and save a new user"""
        if not email:
            raise ValueError('Users must have an email address!')
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model supporting email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Thumbnail(models.Model):
    name = models.CharField(_('name'), max_length=255)
    image = models.ImageField(
        _('image file'),
        max_length=100,
        upload_to=thumbnail_file_path,
    )

    owner = models.ForeignKey(
        User,
        related_name='thumbnails',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('thumnail')
        verbose_name_plural = _('thumnails')
        ordering = ('name',)
