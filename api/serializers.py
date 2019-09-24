from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Patientdata, Patient, Patientguidelines, Patientrecommendations, LANGUAGE_CHOICES, STYLE_CHOICES


class PatientdataSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    patientdata = serializers.HyperlinkedIdentityField(view_name='patientdata-detail', format='html')

    class Meta:
        model = Patientdata
        fields = ('url', 'id', 'patientdata', 'name', 'date', 'gender', 'systolic_BP', 'diastolic_BP', 'smoking_years', 'no_of_packs', 'fasting_blood_sugar',
        'hypothyroid', 'obese', 'intravenous_drug_abuse', 'owner')
       # read_only_fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    api = serializers.HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'api')

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    patient = serializers.HyperlinkedIdentityField(view_name='patient-detail', format='html')

    class Meta:
        model = Patient
        fields = ('url', 'id', 'patient', 'recommendation', 'optional_applicable_conditions', 'references')
        #read_only_fields = '__all__'


class PatientguidelinesSerializer(serializers.HyperlinkedModelSerializer):
    patientguidelines = serializers.HyperlinkedIdentityField(view_name='patientguidelines-detail', format='html')

    class Meta:
        model = Patientguidelines
        fields = ('url', 'id', 'patientguidelines', 'guideline')


class PatientrecommendationsSerializer(serializers.HyperlinkedModelSerializer):
    patientrecommendations = serializers.HyperlinkedIdentityField(view_name='patientrecommendations-detail', format='html')

    class Meta:
        model = Patientrecommendations
        fields = ('url', 'id', 'patientrecommendations', 'recommendations')



