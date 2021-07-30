from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


class Post(models.Model):

    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Название поста')
    text = models.TextField()
    comments = GenericRelation('Comment')

    def __str__(self):
        return self.title


class Comment(models.Model):

    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст комментария')
    parent = models.ForeignKey(
        'self',
        verbose_name="родительский комментарий",
        blank=True,
        null=True,
        related_name='comment_children',
        on_delete=models.CASCADE
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now=True, verbose_name='Дата создания комментария')
    is_child = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    @property
    def get_parent(self):
        if not self.parent:
            return ""
        return self.parent

