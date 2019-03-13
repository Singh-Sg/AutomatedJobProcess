from django.contrib import admin
from job_apply.models import User, Experience, Training, Vacancy, Application
from django.utils.html import format_html
from django.urls import reverse
admin.site.register(Application)
admin.site.register(Experience)
admin.site.register(Training)
admin.site.register(Vacancy)


class UserAdmin(admin.ModelAdmin):
    date_heirarchy = (
        'modified',
    )
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'account_actions'
    )
    
    def account_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Send application</a>&nbsp;',
            reverse('send_application', args=[obj.pk]),
        )
    account_actions.short_description = 'Account Actions'
    account_actions.allow_tags = True

admin.site.register(User, UserAdmin)