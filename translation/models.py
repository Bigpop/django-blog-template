from django.db import models
from django.contrib.auth.models import User

#整个翻译论坛的内容采用二层的树形结构
class Trans(models.Model):
    parent_id = models.IntegerField(default=-1)#-1为根节点，代表原文否则为译文
    title = models.CharField(max_length=200, default='')
    content = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)

    def increase_likes(self):
        self.likes += 1
        self.save(update_fields=['likes'])

    class Meta:
        db_table = 'transforum_object'
        verbose_name = u'翻译'
