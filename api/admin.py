from django.contrib import admin
from .models import Patientdata, Patient, Patientguidelines, Patientrecommendations

admin.site.register(Patientdata)
admin.site.register(Patient)
admin.site.register(Patientguidelines)
admin.site.register(Patientrecommendations)
