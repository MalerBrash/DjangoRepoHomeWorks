from django.db import models


class Project(models.Model):
    """Объект на котором проводят измерения."""

    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.id}:{self.name}'

    class Meta:
        verbose_name = 'Объект измерения'
        verbose_name_plural = 'Объекты измерения'

class Measurement(models.Model):
    """Измерение температуры на объекте."""

    value = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='measurements')
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.project}:{self.value}, {self.created_at}'

    class Meta:
        verbose_name = 'Температура объекта'
        verbose_name_plural = 'Температура объектов'