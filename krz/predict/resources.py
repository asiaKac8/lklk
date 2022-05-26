from import_export import resources
from .models import IrisImportExport


class IrisImportExportResource(resources.ModelResource):
    class Meta:
        model = IrisImportExport