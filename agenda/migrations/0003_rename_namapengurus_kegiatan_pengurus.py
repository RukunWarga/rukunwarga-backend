# Generated by Django 4.2.8 on 2023-12-11 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_kegiatan_namapengurus_alter_kegiatan_waktukegiatan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kegiatan',
            old_name='namaPengurus',
            new_name='pengurus',
        ),
    ]
