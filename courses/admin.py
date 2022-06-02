from django.contrib import admin

from courses.models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'unit_load', 'department',)
    list_filter = ('code',)


admin.site.register(Course, CourseAdmin)
