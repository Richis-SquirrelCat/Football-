from rest_framework import serializers
from .models import *

from rest_framework import serializers
from .models import *


class ScheduleSerializer(serializers.Serializer):
    model = Schedule
    field = '__all__'


class ClubSerializer(serializers.Serializer):
    model = Club
    field = '__all__'


class MainSerializer(serializers.Serializer):
    model = Main
    field = '__all__'


class MediaSerializer(serializers.Serializer):
    model = Media
    field = '__all__'


class NewsSerializer(serializers.Serializer):
    model = News
    field = '__all__'


class FormViewSerializer(serializers.Serializer):
    model = FormView
    field = '__all__'



class BrandSerializer(serializers.Serializer):
    model = Brand
    field = '__all__'


class StatisticaSerializer(serializers.Serializer):
    model = Statistica
    field = '__all__'


class ParticipantSerializer(serializers.Serializer):
    model = Participant
    field = '__all__'


class OpinionSerializer(serializers.Serializer):
    class Meta:
        model = Opinion
        field = '__all__'


class SocialMediaSerializer(serializers.Serializer):
    class Meta:
        model = SocialMedia
        field = '__all__'


class InfoSerializer(serializers.Serializer):
    class Meta:
        model = Info
        field = '__all__'
