from dataclasses import field
from rest_framework import serializers
from .find_object import obj_list

class object_detectionSerializer(serializers.ModelSerializer):

    class meta:
        model=obj_list()
        field=('cap','arr')
