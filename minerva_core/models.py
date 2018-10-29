import os
import uuid

from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField

import isbn_field
from localflavor.in_.forms import *


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('papers', filename)


class Publication(models.Model):
    TYPES_PUBLICATION = (
        ('PR', 'Paper'),
        ('JO', 'Journal'),
    )
    title = models.CharField(max_length=200, verbose_name="Publication Title")
    isbn = isbn_field.ISBNField(blank=True, unique=True , verbose_name="ISBN Number", null=True)
    date = models.DateField(verbose_name="Published Date")
    citations = models.CharField(blank=True, max_length=400, verbose_name="Citations", null=True)
    paper_journal = models.CharField(max_length=2, choices=TYPES_PUBLICATION, verbose_name="Type Of Publication")
    author = models.ManyToManyField('Person', verbose_name="Authors")
    paper_pdf = models.FileField(upload_to=get_file_path,
                                 validators=[FileExtensionValidator(allowed_extensions=['pdf'])])


    def display_authors(self):
        return ', '.join([author.name for author in self.author.all()])
    display_authors.short_description = "Authors"


    @staticmethod
    def autocomplete_search_fields():
        return 'author__name'

    def __str__(self):
        return self.title


class Person(models.Model):
    name = models.CharField(max_length=60)
    
    email = models.EmailField()
    phno = PhoneNumberField(blank=True, default="+91")

    linked_user = models.ForeignKey('authtools.User', on_delete=models.CASCADE, blank=True , verbose_name="Linked User", null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Author Profile'
