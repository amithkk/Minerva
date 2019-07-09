#  Copyright (c) 2018 - Amith K K
#  Released under the GNU GPLv3 License
#

import authtools
from authtools.admin import NamedUserAdmin
from authtools.forms import UserCreationForm
from django.contrib import admin

# Register your models here.
from django.contrib.admin import DateFieldListFilter
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import Group
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.forms import forms
from django.utils.crypto import get_random_string
from django.utils.html import format_html
from jet.filters import DateRangeFilter

from minerva_core.models import Person, Publication


class UserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        # If one field gets autocompleted but not the other, our 'neither
        # password or both password' validation will be triggered.
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'
        self.fields['password2'].widget.attrs['autocomplete'] = 'off'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = super(UserCreationForm, self).clean_password2()
        if bool(password1) ^ bool(password2):
            raise forms.ValidationError("Fill out both fields")
        return password2


User = get_user_model()


class UserAdmin(NamedUserAdmin):
    """
    A UserAdmin that sends a password-reset email when creating a new user,
    unless a password was entered.
    """
    add_form = UserCreationForm
    add_fieldsets = (
        (None, {
            'description': (
                "Enter the new user's name and email address and click save."
                " The user will be emailed a link allowing them to login to"
                " the site and set their password."
            ),
            'fields': ('email', 'name',),
        }),
        ('Password', {
            'description': "Optionally, you may set the user's password here.",
            'fields': ('password1', 'password2'),
            'classes': ('collapse', 'collapse-closed'),
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change and (not form.cleaned_data['password1'] or not obj.has_usable_password()):
            # Django's PasswordResetForm won't let us reset an unusable
            # password. We set it above super() so we don't have to save twice.
            obj.set_password(get_random_string())
            reset_password = True
        else:
            reset_password = False

        if request.user.is_superuser:
            obj.is_staff = True
            obj.save()

        if not change:
            obj.groups.add(Group.objects.get(name='AuthorGroup'))



        super(UserAdmin, self).save_model(request, obj, form, change)

        if reset_password:
            reset_form = PasswordResetForm({'email': obj.email})
            assert reset_form.is_valid()
            reset_form.save(
                request=request,
                use_https=request.is_secure(),
                subject_template_name='minv_reg/email_sub.txt',
                email_template_name='minv_reg/email_body.html',
            )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class PersonAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Person, PersonAdmin)


class PublicationAdmin(admin.ModelAdmin):
    #   autocomplete_fields = ['author']
    list_display = ('title', 'display_authors', 'date', 'isbn', 'download_pdf')
    search_fields = ('title', 'author__name')
    list_filter = (('date', DateRangeFilter), ('paper_journal'))

    def download_pdf(self, obj):
        return format_html("<a href='{0}' target='_blank'><img "
                           "src='{1}' height=40px></a>",
                           obj.paper_pdf.url, static('img/ic_pdf.png'))

    def get_queryset(self, request):
        qs = super(PublicationAdmin, self).get_queryset(request)
        if not (request.user.is_superuser or request.user.email=='nmit_student@nmit.ac.in'):
            qs = qs.filter(author__linked_user=request.user)
        return qs

    def changelist_view(self, request, extra_context=None):
        print("Changelist View")
        return super(PublicationAdmin, self).changelist_view(request, extra_context)


admin.site.register(Publication, PublicationAdmin)
