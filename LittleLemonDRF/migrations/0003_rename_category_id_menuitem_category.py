# Generated by Django 4.1.4 on 2023-01-02 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonDRF', '0002_rename_category_menuitem_category_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='category_id',
            new_name='category',
        ),
    ]
