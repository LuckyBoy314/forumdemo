# coding: utf-8
from django.contrib.auth.models import User
from django.db import models


class ActivateCode(models.Model):
    owner = models.ForeignKey(User, verbose_name=u"用户")
    code = models.CharField(u"激活码", max_length=100)

    expire_timestamp = models.DateTimeField()

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)


class UserProfile(models.Model):
    owner = models.ForeignKey(User, verbose_name=u"用户")
    avatar = models.CharField(u"头像地址", max_length=300, blank=True)

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)
