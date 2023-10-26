# Generated by Django 4.2.4 on 2023-10-01 22:04

import django.core.validators
from django.db import migrations, models
import signup.models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0009_page_setting_delete_appmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page_setting',
            old_name='footertext',
            new_name='footer_text',
        ),
        migrations.RemoveField(
            model_name='page_setting',
            name='number',
        ),
        migrations.RemoveField(
            model_name='page_setting',
            name='pagelogo',
        ),
        migrations.RemoveField(
            model_name='page_setting',
            name='signuplogo',
        ),
        migrations.AddField(
            model_name='page_setting',
            name='admin_login_image',
            field=models.ImageField(default='assets/img/logo.png', upload_to='assets/img/'),
        ),
        migrations.AddField(
            model_name='page_setting',
            name='admin_page_logo',
            field=models.ImageField(default='assets/img/logo.png', upload_to='assets/img/'),
        ),
        migrations.AddField(
            model_name='page_setting',
            name='chat_color',
            field=signup.models.Color(default=2, max_length=7, validators=[django.core.validators.RegexValidator(code='invalid_color', message='Enter a valid color code in hexadecimal format (e.g., #RRGGBB or #RGB).', regex='^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')]),
        ),
        migrations.AddField(
            model_name='page_setting',
            name='login_page_logo',
            field=models.ImageField(default='assets/img/logo.png', upload_to='assets/img/'),
        ),
        migrations.AlterField(
            model_name='page_setting',
            name='email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='page_setting',
            name='favicon',
            field=models.ImageField(default='assets/img/logo.png', upload_to='assets/img/'),
        ),
    ]
