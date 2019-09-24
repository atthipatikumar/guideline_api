from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view
from api import views

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    path('schema/', schema_view),
    path('api/', views.PatientList.as_view(), name='patient-list'),
    path('api/<int:pk>/', views.PatientDetail.as_view(), name='patient-detail'),
    path('api/<int:pk>/highlight/', views.PatientHighlight.as_view(), name='patient-highlight'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('api2/', views.PatientdataList.as_view(), name='patientdata-list'),
    path('api2/<int:pk>/', views.PatientdataDetail.as_view(), name='patientdata-detail'),
    path('api2/<int:pk>/highlight/', views.PatientdataHighlight.as_view(), name='patientdata-highlight'),
    path('api3/', views.PatientguidelinesList.as_view(), name='patientguidelines-list'),
    path('api3/<int:pk>/', views.PatientguidelinesDetail.as_view(), name='patientguidelines-detail'),
    path('api3/<int:pk>/highlight/', views.PatientguidelinesHighLight.as_view(), name='patientguidelines-highlight'),
    path('api4/', views.PatientrecommendationsList.as_view(), name='patientrecommendations-list'),
    path('api4/<int:pk>/', views.PatientrecommendationsDetail.as_view(), name='patientrecommendations-detail'),
    path('api4/<int:pk>/highlight/', views.PatientrecommendationsHighLight.as_view(), name='patientrecommendations-highlight'),
    path('', views.api_root),

]

urlpatterns = format_suffix_patterns(urlpatterns)