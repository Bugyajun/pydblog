from __future__ import absolute_import, unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth import authenticate


class user(models.Model):
    user_name = models.CharField(max_length=100)
    user_password = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name
