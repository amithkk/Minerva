# Generated by Django 2.1.2 on 2018-10-21 08:28

import django.core.validators
from django.db import migrations, models
import minerva_core.models


class Migration(migrations.Migration):

    dependencies = [
        ('minerva_core', '0002_publication_paper_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='paper_pdf',
            field=models.FileField(upload_to=minerva_core.models.get_file_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]
