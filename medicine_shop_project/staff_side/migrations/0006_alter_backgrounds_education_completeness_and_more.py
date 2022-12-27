# Generated by Django 4.1.4 on 2022-12-27 05:40

from django.db import migrations, models
import staff_side.models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_side', '0005_remove_backgrounds_full_education_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backgrounds',
            name='education_completeness',
            field=models.CharField(choices=[(staff_side.models.EducationCompleteness['FULL'], 'Полное'), (staff_side.models.EducationCompleteness['NOT_FULL'], 'Неполное')], default=staff_side.models.EducationCompleteness['FULL'], max_length=50, verbose_name='Полнота образования'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='schedule_type',
            field=models.CharField(choices=[(staff_side.models.Schedule['FLEXIBLE'], 'Гибкий график'), (staff_side.models.Schedule['FULL_TIME'], 'Полный день'), (staff_side.models.Schedule['PART_TIME'], 'Частичная занятость')], default=staff_side.models.Schedule['FULL_TIME'], max_length=250, verbose_name='Расписание'),
        ),
    ]
