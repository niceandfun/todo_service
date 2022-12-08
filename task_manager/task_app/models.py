from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=1000, verbose_name='Название')
    description = models.TextField(default='', verbose_name='Описание')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата изменения')
    author = models.ForeignKey('Author', default=None, null=True, verbose_name='Автор задачи', related_name='author',
                               on_delete=models.CASCADE)
    status = models.ForeignKey('TaskStatus', default=None, null=True, verbose_name='Статус задачи',
                               related_name='author',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task'
        ordering = ['title']


class Author(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'author'


class TaskStatus(models.Model):
    status = models.CharField()

    def __str__(self):
        return self.status

    class Meta:
        db_table = 'task_status'
