from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializer import ContactsSerializer
from .models import Contacts
from rest_framework import permissions
from rest_framework.response import Response


class ListCreateContact(ListCreateAPIView):

    serializer_class = ContactsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Contacts.objects.filter(owner=self.request.user)


class ListAllUserContacts(ListCreateAPIView):

    serializer_class = ContactsSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Contacts.objects.all()


class DetailContact(RetrieveUpdateDestroyAPIView):

    serializer_class = ContactsSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id' 

    def get_queryset(self):
        return Contacts.objects.filter(owner=self.request.user)
    
