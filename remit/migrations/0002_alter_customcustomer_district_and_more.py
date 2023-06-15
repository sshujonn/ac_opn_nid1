# Generated by Django 4.1.2 on 2023-06-14 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customcustomer',
            name='district',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='customcustomer',
            name='division',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='customcustomer',
            name='dob',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='customcustomer',
            name='f_name',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='customcustomer',
            name='m_name',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='customcustomer',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='customcustomer',
            name='occupation',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='customcustomer',
            name='post_office',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='customcustomer',
            name='s_name',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='customcustomer',
            name='thana',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='customcustomer',
            name='village',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]
