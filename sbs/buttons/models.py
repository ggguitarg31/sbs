from django.db import models
from django.contrib.auth.models import User


class ButtonCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    cover = models.ImageField(upload_to='button_category', blank=True)
    about = models.TextField(max_length=400, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Button Categories"


class Tags(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "tags"


class Qualities(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "qualities"


class Button(models.Model):
    model_no = models.CharField(max_length=5, unique=True)
    image = models.ImageField(upload_to='buttons')
    size = models.IntegerField(choices=[(i, i) for i in range(14, 37)], default=14)
    qualities = models.ManyToManyField(Qualities, related_name='qualities', blank=True)
    button_type = models.ManyToManyField(ButtonCategory, related_name='btn_category')
    date_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    price_unit = models.IntegerField(default=1, blank=True, null=True)
    tags = models.ManyToManyField(Tags, related_name='tags', blank=True)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ['model_no']

    def __str__(self):
        return self.model_no
