from django.urls import path
from .views import ListCreateContact,DetailContact,ListAllUserContacts

urlpatterns = [
    path('list', ListCreateContact.as_view()),
    path('<int:id>', DetailContact.as_view()),
    path('allcontacts', ListAllUserContacts.as_view()),
]