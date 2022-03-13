from rest_framework.serializers import ModelSerializer
from .models import Contacts


class ContactsSerializer(ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['id','first_name','last_name','country_code','phone_number','contact_picture','is_favourite']


