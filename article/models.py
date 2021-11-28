from django.db import models
# from tinymce.models import HTMLField
# from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField
from martor.models import MartorField

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = MartorField()
    c_time = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
        return ''

    class Meta:
        db_table = 'article'
        verbose_name = u'文章'
