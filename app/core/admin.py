from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import Plan, Thumbnail, User


class UserAdmin(BaseUserAdmin):
    ordering = ('id',)
    list_display = ('email', 'name')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
        (_('Plant type'), {'fields': ('plan',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'plan')
        })
    )


admin.site.register(User, UserAdmin)
admin.site.register(Plan)
admin.site.register(Thumbnail)
