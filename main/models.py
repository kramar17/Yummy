from django.db import models
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField


# Create your models here.
class DishCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()

    def __iter__(self):
        for dish in self.dishes.filter(is_visible=True):
            yield dish

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія страв'
        verbose_name_plural = 'Категорії страв'
        ordering = ['-sort']


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    ingredients = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE, related_name='dishes')
    sort = models.PositiveSmallIntegerField()

    photo = models.ImageField(upload_to='dishes/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страва'
        verbose_name_plural = 'Страви'
        ordering = ['sort']


class Gallery(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
        ordering = ['name']


class Reservation(models.Model):
    phone_regex = RegexValidator(regex=r'\+?(380)?0?d{7}$', message='Phone number must be entered in the format: +380xxxxxxx')
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, validators=[phone_regex])
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    count = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    is_confirmed = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.date} - {self.time}'

    class Meta:
        verbose_name = 'Бронювання'
        verbose_name_plural = 'Бронювання'
        ordering = ['-date_created']


class EventsImage(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='events/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фото івенту'
        verbose_name_plural = 'Фото івентів'
        ordering = ['name']


class Staff(models.Model):
    POSITION_CHOICES = [
        ('kitchen', 'kitchen'),
        ('bar', 'bar'),
        ('waiter', 'waiter'),
        ('manager', 'manager')
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    position = models.CharField(max_length=10, choices=POSITION_CHOICES)
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='staff/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'
        ordering = ['position']
