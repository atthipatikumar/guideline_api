from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .permissions import IsOwnerOrReadOnly
from .models import Patientdata, Patient, Patientguidelines, Patientrecommendations
from .serializers import UserSerializer, PatientdataSerializer, PatientSerializer, PatientguidelinesSerializer, PatientrecommendationsSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'api': reverse('api-list', request=request, format=format)
    })

class PatientdataHighlight(generics.GenericAPIView):
    queryset = Patientdata.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer)

    def get(self, request, *args, **kwargs):
        patientdata = self.get_object()
        return Response(patientdata.data)

class PatientdataList(generics.ListCreateAPIView):
    queryset = Patientdata.objects.all()
    serializer_class = PatientdataSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PatientdataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patientdata.objects.all()
    serializer_class = PatientdataSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PatientHighlight(generics.GenericAPIView):
    queryset = Patient.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer)

    def get(self, request, *args, **kwargs):
        patient = self.get_object()
        return Response(patient.data)

class PatientList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def List1(self, request):
        queryset = self.get_queryset()
        serializer = PatientSerializer(queryset, many=True)
        return Response(serializer.data)

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class PatientguidelinesHighLight(generics.GenericAPIView):
    queryset = Patientguidelines.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer)

    def get(self, request, *args, **kwargs):
        patientguidelines = self.get_object()
        return Response(patientguidelines.data)
class PatientguidelinesList(generics.ListCreateAPIView):
    queryset = Patientguidelines.objects.all()
    serializer_class = PatientguidelinesSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def List2(self, request):
        queryset = self.get_queryset()
        seializer = PatientguidelinesSerializer(queryset, many=True)
        return Response(seializer.data)

class PatientguidelinesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patientguidelines.objects.all()
    serializer_class = PatientguidelinesSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)


class PatientrecommendationsHighLight(generics.GenericAPIView):
    queryset = Patientrecommendations.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer)

class PatientrecommendationsList(generics.ListCreateAPIView):
    queryset = Patientrecommendations.objects.all()
    serializer_class = PatientrecommendationsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def List(self, request):
        queryset = self.get_queryset()
        serializer = PatientrecommendationsSerializer(queryset, many=True)
        return Response(serializer.data)

class PatientrecommendationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patientrecommendations.objects.all()
    serializer_class = PatientrecommendationsSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

