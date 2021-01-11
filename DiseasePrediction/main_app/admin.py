from django.contrib import admin
from .models import patient , doctor , diseaseinfo , consultation,rating_review

# Register your models here.


class PatientrAdmin(admin.ModelAdmin):
    list_display = ("name", "dob", "address","mobile_no","gender","user","is_patient")
    list_filter =("name",)
    search_fields = ('name', )
    list_per_page = 10
admin.site.register(patient,PatientrAdmin)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "dob", "address","mobile_no","gender","user","qualification","specialization","is_doctor")
    list_filter =("name",)
    search_fields = ('name', )
    list_per_page = 10
admin.site.register(doctor,DoctorAdmin)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ("patient","diseasename", "no_of_symp","symptomsname","confidence","consultdoctor")
    list_filter =("patient",)
    search_fields = ('patient', )
    list_per_page = 10
admin.site.register(diseaseinfo,DiseaseAdmin)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ("patient", "doctor", "diseaseinfo","consultation_date","status")
    list_filter =("doctor",)
    search_fields = ('doctor', )
    list_per_page = 10
admin.site.register(consultation, ConsultationAdmin)
admin.site.register(rating_review)