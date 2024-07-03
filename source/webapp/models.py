from django.db import models

statuses = [("new", "Новая"), ("moderated", "Модерированная"), ("deleted", "Удаленная")]


class Article(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="Название")
    author = models.CharField(max_length=50, null=False, blank=False, verbose_name="Автор", default="Неизвестный")
    content = models.TextField(max_length=1000, null=False, blank=False, verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    status = models.CharField(max_length=25, choices=statuses, verbose_name="Статус", default=statuses[0][0])

    def __str__(self):
        return f"{self.pk}. {self.title}: {self.author}"

    class Meta:
        db_table = "articles"
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"