from rest_framework import serializers
from .models import Final_Year_Projects
from taggit.models import Tag
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
import six


class NewTagListSerializerField(TagListSerializerField):
    def to_internal_value(self, value):
        if isinstance(value, six.string_types):
            value = value.split(',')

        if not isinstance(value, list):
            self.fail('not_a_list', input_type=type(value).__name__)

        for s in value:
            if not isinstance(s, six.string_types):
                self.fail('not_a_str')

            self.child.run_validation(s)
        return value


class FYPSerializer(TaggitSerializer, serializers.ModelSerializer):
    Students = NewTagListSerializerField()

    class Meta:
        model = Final_Year_Projects
        fields = ("id", "BatchYear", "Project_Name", "Project_Supervisor",
                  "External_Supervisor", "Co_Supervisor", "Project_Id", "Students")
