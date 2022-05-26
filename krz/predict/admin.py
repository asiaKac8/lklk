from django.contrib import admin

# iris prediction
from .models import PredictionResults, Zbior
@admin.register(PredictionResults)
class PredictionResultsAdmin(admin.ModelAdmin):
    list_display = ['id','sepal_length','sepal_width','petal_length','petal_width','classification']
    list_filter = ['classification']

# universal db 

from .models import Atrybut
from .models import Dana
from .models import Obserwacja
from .models import Klasa
from .models import Zbior


admin.site.register(Dana)
admin.site.register(Obserwacja)
admin.site.register(Klasa)

@admin.register(Zbior)
class ZbiorAdmin(admin.ModelAdmin):
    pass

@admin.register(Atrybut)
class AtrybutAdmin(admin.ModelAdmin):
    search_fields = ['nazwa']
    list_display = ['id_atrybut','nazwa','id_zbior']
    list_filter = ['id_zbior']


# iris import export
from import_export.admin import ImportExportModelAdmin
from .models import IrisImportExport
admin.site.register(IrisImportExport)


# universal table
from .models import UniversalTable
admin.site.register(UniversalTable)

