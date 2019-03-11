from rest_framework import serializers
from .models import Language, Paradigm, Programmer


# class LanguageSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Language
#         fields = ('id', 'url', 'name', 'paradigm')

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'url', 'name', 'paradigm')
        # fields = ('id', 'name', 'paradigm')


class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        fields = ('id', 'url', 'name')
        #fields = ('id', 'name')


class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmer
        fields = ('id', 'url', 'name', 'languages')
        #fields = ('id', 'name', 'languages')
