from django.contrib import admin

from questions.models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'course',)
    list_filter = ('course',)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
