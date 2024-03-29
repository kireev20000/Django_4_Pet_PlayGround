"""Модели для приложения Post."""

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    """Кастомный менеджер для вывода кварисета со статусом опубликовано."""

    def get_queryset(self):
        """Возвращает кастомный кварисет с опубликоваными постами."""
        return super().get_queryset() \
            .filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    """Модель Post для блога."""

    class Status(models.TextChoices):
        """Захардкоженные статусы поста."""

        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(
        max_length=250,
        verbose_name='Заголовок',
        help_text='Введите заголовок',
    )
    slug = models.SlugField(
        max_length=250,
        unique_for_date='publish',
    )
    body = models.TextField(
        'Текст поста',
        help_text='Введите текст поста',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts',
        verbose_name='Автор',
    )
    publish = models.DateTimeField(
        'Дата публикации',
        default=timezone.now,
    )
    created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        'Дата последнего изменения',
        auto_now=True,
    )
    status = models.CharField(
        'Статус',
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    # первый объявленый менеджер становится дефолтным
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        """Обожаю Flake8 тут. Класс мета модели пост."""

        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        """Возвращает канонический URL поста."""
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

    def __str__(self):
        """Возвращает заголовок поста."""
        return self.title


class Comments(models.Model):
    """Модель комментариев к посту."""

    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments',
                             verbose_name='Пост')
    name = models.CharField(max_length=80, verbose_name='Автор')
    email = models.EmailField(verbose_name='E-mail')
    body = models.TextField(verbose_name='Комментарий')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан:')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен:')
    active = models.BooleanField(default=True, verbose_name='Показывать')

    class Meta:
        """Класс Мета модели Comments."""

        ordering = ['created']
        indexes = [models.Index(fields=['created']), ]
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        """Возвращает инфу о комменте."""
        return f'Комментарий {self.name} на пост "{self.post}"'
