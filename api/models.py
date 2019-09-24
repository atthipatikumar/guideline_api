# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Patientdata(models.Model):
    #id = models.CharField(max_length=10, primary_key=True, unique=True)
    name = models.CharField(max_length=350)
    date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10)
    systolic_BP = models.IntegerField()
    diastolic_BP = models.IntegerField()
    smoking_years = models.IntegerField()
    no_of_packs = models.IntegerField()
    fasting_blood_sugar = models.IntegerField()
    hypothyroid = models.CharField(max_length=5)
    obese = models.CharField(max_length=5)
    intravenous_drug_abuse = models.CharField(max_length=5)
    owner = models.ForeignKey('auth.User', related_name='api', on_delete=models.CASCADE)

    #class Meta:
      #  ordering = ['name']

    def __str__(self):
        return self.name


class Patient(models.Model):
    #id = models.CharField(max_length=10, primary_key=True, unique=True)
    recommendation = models.CharField(max_length=2000)
    optional_applicable_conditions = models.CharField(max_length=2000)
    references = models.CharField(max_length=2000)

    #class Meta:
       # ordering = ['recommendation']

    def __str__(self):
        return self.recommendation



class Patientguidelines(models.Model):
    guideline = models.ForeignKey(Patient, verbose_name="Recommendations", on_delete=models.CASCADE)


class Patientrecommendations(models.Model):
    recommendations = models.ForeignKey(Patient, verbose_name="Recommendations", on_delete=models.CASCADE)
    #conditions = models.CharField(max_length=5, default="SOME STRING", editable=False)
    #references = models.CharField(max_length=500)

    #def __str__(self):
     #  return self.references
