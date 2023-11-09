from django.db import models


class Scopes(models.Model):
    Tag = models.TextField(verbose_name='Тэг') 
    is_main = models.BooleanField(verbose_name='Основной')
    
    class Meta:
        verbose_name = 'Тэги'


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField(Scopes, related_name='articles')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
    


