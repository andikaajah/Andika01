# Generated by Django 4.2.6 on 2023-11-12 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.CharField(max_length=100)),
                ('keterangan', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Fotoproduk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Kategori',
        ),
        migrations.DeleteModel(
            name='Produk',
        ),
    ]