from django.db import models

# Create your models here.


class ItemCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True, primary_key=True)
    oily = models.CharField(max_length=1000, blank=True)
    sensitive = models.CharField(max_length=1000, blank=True)
    dry = models.CharField(max_length=1000, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'



class Item(models.Model):
    CATEGORY = (
        ('skincare', '스킨케어'),
        ('maskpack', '마스크팩'),
        ('suncare', '선케어'),
        ('basemakeup', '베이스메이크업')
    )
    GENDER = (
        ('male', 'male'),
        ('female', 'female'),
        ('all', 'all')
    )

    id = models.IntegerField(primary_key=True)
    imageId = models.ImageField(max_length=1000)
    name = models.CharField(max_length=1000)
    price = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER)
    category = models.CharField(max_length=10, choices= CATEGORY)
    ingredients = models.ManyToManyField(ItemCategory, related_name='item_ing')
    monthlySales = models.IntegerField()

    class Meta:
        ordering = ['id']
        verbose_name = 'cosmetic'
        verbose_name_plural = 'cosmetics'

    def __str__(self):
        return self.name