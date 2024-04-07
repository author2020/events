from rest_framework import serializers

from events.models import Event, Subevent, Speaker


class SpeakerSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для спикера.
    '''
    subevent = serializers.StringRelatedField(many=True, read_only=True)
    full_name = serializers.SerializerMethodField()

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

