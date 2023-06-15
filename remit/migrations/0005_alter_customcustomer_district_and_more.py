# Generated by Django 4.1.2 on 2023-06-14 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remit', '0004_rename_f_name_customcustomer_father_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customcustomer',
            name='district',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customcustomer',
            name='division',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customcustomer',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customcustomer',
            name='father_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customcustomer',
            name='mother_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customcustomer',
            name='occupation',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customcustomer',
            name='post_office',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customcustomer',
            name='spouse_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customcustomer',
            name='thana',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customcustomer',
            name='village',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
