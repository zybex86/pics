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

    def create_user(self, email, plan_type, password=None, **kwargs):
        """Create and save a new user"""
        if not email:
            raise ValueError('Users must have an email address!')
        if not plan_type:
            raise ValueError('Each user must have a plan!')
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.plan = Plan.objects.get(id=plan_type)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, plan_type, password):
        user = self.create_user(email, plan_type, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class Plan(models.Model):
    id = models.CharField(_('ID'), max_length=1, primary_key=True)
    name = models.CharField(_('name'), max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('plan type')
        verbose_name_plural = _('plan types')
        ordering = ('id',)


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model supporting email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    plan = models.ForeignKey(
        Plan,
        verbose_name=_('plan'),
        on_delete=models.PROTECT,
        default='B'
    )

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
        verbose_name = _('thumbnail')
        verbose_name_plural = _('thumbnails')
        ordering = ('name',)
