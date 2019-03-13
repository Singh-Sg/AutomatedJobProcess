from django.contrib import admin
from .models import Report



class ReportAdmin(admin.ModelAdmin):
    """
    """
    list_display = (
        'id',
        'user',
        'vacancy',
        'result',
    )

admin.site.register(Report, ReportAdmin)
