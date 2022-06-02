from django.contrib import admin

from users.models import CustomUser, Department, Lecturer, Students


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('reg_no', 'email', 'first_name', 'last_name', 'is_admin',)
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'reg_no', 'email', 'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    search_fields = ('email', 'reg_no',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'department', 'reg_date',)


class LecturerAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'reg_date',)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(Students, StudentAdmin)
