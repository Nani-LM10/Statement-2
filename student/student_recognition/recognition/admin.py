from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Faculty
from .models import Student, StudentRank

admin.site.register(Faculty)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'admission_batch', 'academic_performance', 'consistency', 'core_courses_excellence', 'hackathon_participation', 'paper_presentations', 'teacher_assistance')
    search_fields = ['user__username', 'admission_batch']
    list_filter = ('admission_batch',)

class StudentRankAdmin(admin.ModelAdmin):
    list_display = ('student', 'score', 'rank')
    search_fields = ['student__user__username']
    list_filter = ('rank',)
 
admin.site.register(Student, StudentAdmin)
admin.site.register(StudentRank, StudentRankAdmin)

