# Generated by Django 2.2.4 on 2020-01-18 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('name', models.CharField(db_index=True, max_length=100, primary_key=True, serialize=False)),
                ('oily', models.CharField(blank=True, max_length=1000)),
                ('sensitive', models.CharField(blank=True, max_length=1000)),
                ('dry', models.CharField(blank=True, max_length=1000)),
            ],
            options={
                'verbose_name': 'ingredient',
                'verbose_name_plural': 'ingredients',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('imageId', models.ImageField(max_length=1000, upload_to='')),
                ('name', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('all', 'all')], max_length=10)),
                ('category', models.CharField(choices=[('skincare', '스킨케어'), ('maskpack', '마스크팩'), ('suncare', '선케어'), ('basemakeup', '베이스메이크업')], max_length=10)),
                ('monthlySales', models.IntegerField()),
                ('ingredients', models.ManyToManyField(related_name='item_ing', to='item.ItemCategory')),
            ],
            options={
                'verbose_name': 'cosmetic',
                'verbose_name_plural': 'cosmetics',
                'ordering': ['id'],
            },
        ),
    ]
