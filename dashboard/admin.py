from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from dashboard.resources import PropertyAdminResource
# Register your models here.
from dashboard.models import AddBook
class AddbookAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = PropertyAdminResource
    
    
admin.site.register(AddBook,AddbookAdmin)