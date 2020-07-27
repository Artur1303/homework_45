from django.db import models

STATUS_CHOICES = [
    ('new', 'Новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Сделано')
]


class Todo(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='new', verbose_name='статус')
    descriptions = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    data = models.DateField(null=True, blank=True, verbose_name='Время завершение')

    def __str__(self):
        return "{}. {}".format(self.pk, self.title)

    class Meta:
        verbose_name = 'Задачи'
        verbose_name_plural = 'Задача'
