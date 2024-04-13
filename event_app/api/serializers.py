from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.validators import RegexValidator

from events.models import Event, Subevent, Speaker


class SpeakerSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для спикера.
    '''
    subevent = serializers.StringRelatedField(many=True, read_only=True)
    full_name = serializers.SerializerMethodField()
    first_name = serializers.CharField(validators=[RegexValidator(
        regex=r'^[a-zA-Zа-яА-Я]+$',
        message='Имя может содержать только русские либо латинские буквы!')])
    last_name = serializers.CharField(validators=[RegexValidator(
        regex=r'^[a-zA-Zа-яА-Я\-]+$',
        message='Фамилия может содержать только русские либо латинские'
                ' буквы, а также тире!')])
    contacts = serializers.CharField(
        validators=[UniqueValidator(queryset=Speaker.objects.all())]
    )

    class Meta:
        model = Speaker
        fields = '__all__'

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class SubeventSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для части программы.
    '''
    event = serializers.StringRelatedField(read_only=True)
    speaker = SpeakerSerializer(read_only=True)

    class Meta:
        fields = '__all__'
        model = Subevent


class EventSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для мероприятия.
    '''
    subevents = SubeventSerializer(many=True, read_only=True)
    participants = serializers.StringRelatedField(many=True, read_only=True)


    class Meta:
        model = Event
        fields = '__all__'

