# Generated by Django 4.0.6 on 2022-08-25 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_alter_currency_symbol_alter_currency_country_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='CVV_security_code',
            new_name='cvv_security_code',
        ),
        migrations.RenameField(
            model_name='currency',
            old_name='Symbol',
            new_name='symbol',
        ),
        migrations.RemoveField(
            model_name='receipt',
            name='receipt_file',
        ),
    ]
