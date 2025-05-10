from django.db import models


class Typephoto(models.Model):
    size = models.CharField(max_length=120)
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Тип фото'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.size
