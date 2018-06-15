# from __future__ import unicode_literals
# from django.utils.encoding import python_2_unicode_compatible


from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.base_user import BaseUserManager





class AuthUserManager(BaseUserManager):
    """ユーザーマネージャー"""

    use_in_migrations = True


    def _create_user(self, name, password, **extra_fields):
        """
        ユーザ作成

        :param password: パスワード
        :param name: 名前
        :return: AuthUserオブジェクト
        """

        if not name:
            raise ValueError('Users must have an name')

        user = self.model(name=name, **extra_fields)

        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user



    def create_user(self,name, password=None, **extra_fields):
        """is_staff(管理サイトにログインできるか)と、is_superuer(全ての権限)をFalseに"""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name, password, **extra_fields)


    def create_superuser(self, name, password, **extra_fields):
        """スーパーユーザーは、is_staffとis_superuserをTrueに"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(name, password, **extra_fields)



class user(AbstractBaseUser, PermissionsMixin):
    """
    ユーザ情報を管理する
    """
    class Meta:
        verbose_name = 'ユーザ'
        verbose_name_plural = 'ユーザ'

    def get_short_name(self):
        """
        ユーザの名前を取得する

        :return: 苗字
        """
        return self.name



    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    # password = models.CharField(max_length=20)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )


    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []
    objects = AuthUserManager()

    def __str__(self):
        return self.name

class teacher(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)


class classes(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    weekNum = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    timeNum = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    teacherId = models.ForeignKey(teacher,on_delete=models.DO_NOTHING)
    place = models.CharField(max_length=10)


class table(models.Model):

    id = models.IntegerField(primary_key=True)
    userId = models.ForeignKey(user,on_delete=models.DO_NOTHING)
    classId = models.ForeignKey(classes,on_delete=models.DO_NOTHING)







##########templatesの中でfor文を回すためのテーブル##############
class time(models.Model):
    num = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])

class week(models.Model):
    num = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)])
