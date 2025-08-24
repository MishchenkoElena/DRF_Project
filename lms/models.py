from django.core.validators import URLValidator
from django.db import models


class Course(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование курса",
        help_text="Введите наименование курса",
    )
    description = models.TextField(
        max_length=100,
        verbose_name="Описание курса",
        help_text="Введите описание курса",
    )

    preview = models.ImageField(
        upload_to="lms/preview",
        blank=True,
        null=True,
        verbose_name="Превью(изображение)",
        help_text="Загрузите фото(изображение)",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

        def __str__(self):
            return self.name


class Lesson(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование урока",
        help_text="Введите наименование урока",
    )
    description = models.TextField(
        max_length=200,
        verbose_name="Описание урока",
        help_text="Введите описание урока",
    )

    preview = models.ImageField(
        upload_to="lms/preview",
        blank=True,
        null=True,
        verbose_name="Превью(изображение)",
        help_text="Загрузите изображение",
    )

    video = models.URLField(
        max_length=200,
        validators=[URLValidator()],
        help_text="Введите полный URL",
        unique=True,
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Наименование курса",
        help_text="Введите наименование курса",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.name
