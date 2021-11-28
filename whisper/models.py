from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from martor.models import MartorField


class Whisper(models.Model):
    content = MartorField()
    c_time = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:40]

    class Meta:
        db_table = 'whisper'
        verbose_name = u'碎碎念'
