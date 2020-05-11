from rest_framework import serializers
from . models import employees

class employeesSerializers(serializers.ModelSerializer):

    class Meta:
        model=employees
        fields='__all__'
        # fields=('firstname','lastname') We can Also choose custom fiels by doing this
