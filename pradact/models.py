from django.db import models

# Create your models here.

class Pradact(models.Model):
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
    name = models.CharField(verbose_name='название', max_length=100)
    image = models.ImageField(verbose_name='изображение', upload_to='pradact_images/')
    category = models.ForeignKey(
        'pradact.Category', on_delete=models.PROTECT, related_name='pradact', verbose_name='категория')
    tags = models.ManyToManyField('pradact.Tag', related_name='pradact', verbose_name='теги')
    description = models.CharField(verbose_name='описание', max_length=300)
    price = models.PositiveIntegerField(verbose_name='сом', default=0)
    is_published = models.BooleanField(verbose_name='публичность', default=True)
class Category(models.Model):

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
    image = models.ImageField(verbose_name='изображение', upload_to='pradact_images/',)
    name = models.CharField(verbose_name='название', max_length=100)
    def __str__(self):
        return f'{self.name}'

class Tag(models.Model):
    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    name = models.CharField(verbose_name='название', max_length=100)

    def __str__(self):
        return f'{self.name}'
    
