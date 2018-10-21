from django.contrib import admin

# Register your models here.
from django.contrib.admin import DateFieldListFilter
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html
from jet.filters import DateRangeFilter

from admin_view_permission.admin import AdminViewPermissionModelAdmin
from minerva_core.models import Person, Publication


class PersonAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Person, PersonAdmin)


class PublicationAdmin(AdminViewPermissionModelAdmin):
    #   autocomplete_fields = ['author']
    list_display = ('title', 'display_authors', 'date', 'isbn', 'download_pdf')
    search_fields = ('title', 'author__name')
    list_filter = (('date', DateRangeFilter),('paper_journal'))



    def download_pdf(self, obj):
        return format_html("<a href='{0}' target='_blank'><img "
                           "src='{1}' height=40px></a>",
                           obj.paper_pdf.url, static('img/ic_pdf.png'))


admin.site.register(Publication, PublicationAdmin)
