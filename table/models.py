from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

saa



class user(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


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


class AuthUserManager(BaseUserManager):
    def create_user(self, name, password):
        """
        ユーザ作成

        :param username: ユーザID
        :param password: パスワード
        :param first_name: 名前
        :return: AuthUserオブジェクト
        """

        if not username:
            raise ValueError('Users must have an username')

        user = self.model(name=name,
                          password=password)

        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user
