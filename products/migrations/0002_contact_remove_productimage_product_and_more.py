# Generated by Django 5.0.1 on 2024-01-29 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.TextField()),
                ('added_on', models.DateField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Contact Table',
            },
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.DeleteModel(
            name='ProductMetaInformation',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]