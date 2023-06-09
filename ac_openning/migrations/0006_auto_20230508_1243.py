# Generated by Django 3.1.7 on 2023-05-08 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ac_openning', '0005_auto_20230508_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='occupation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ac_openning.occupation'),
        ),
    ]
