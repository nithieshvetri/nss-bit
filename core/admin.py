from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models

admin.site.site_header = "NSS-BIT ADMINISTRATION"
admin.site.site_title = "NSS-BIT ADMINISTRATION"
admin.site.index_title = "ADMIN SITE"

class UserAdmin(BaseUserAdmin):
    ordering = ['id'] 
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name', )}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Home)
admin.site.register(models.Services)
admin.site.register(models.UpcomingEvent)
admin.site.register(models.Structure)
admin.site.register(models.POs)
admin.site.register(models.AC)
admin.site.register(models.PMY)
#admin.site.register(models.DL)
admin.site.register(models.NLM)
#admin.site.register(models.SBM)
admin.site.register(models.UBA)
admin.site.register(models.Awards)
admin.site.register(models.Reports)
admin.site.register(models.ActivityCalendar)
admin.site.register(models.Assets)
admin.site.register(models.VT)
#admin.site.register(models.Sapling)
admin.site.register(models.BDC)
admin.site.register(models.Camp)
admin.site.register(models.Seminar)
admin.site.register(models.Others)
admin.site.register(models.HomeUpdate)
