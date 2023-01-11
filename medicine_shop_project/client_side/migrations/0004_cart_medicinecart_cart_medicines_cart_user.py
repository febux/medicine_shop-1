# Generated by Django 4.1.4 on 2023-01-11 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client_side', '0003_alter_medicine__price_increment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('session_key', models.CharField(max_length=255, unique=True, verbose_name='Key')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
        migrations.CreateModel(
            name='MedicineCart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('_amount', models.IntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_side.cart')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_side.medicine')),
            ],
            options={
                'unique_together': {('medicine', 'cart')},
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='medicines',
            field=models.ManyToManyField(through='client_side.MedicineCart', to='client_side.medicine', verbose_name='Лекарства'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
