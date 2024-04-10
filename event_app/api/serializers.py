from rest_framework import serializers

from events.models import Event, EventRegistration, Speaker, Subevent


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
    speaker = SpeakerSerializer(read_only=True)

    class Meta:
        fields = '__all__'
        model = Subevent


class EventSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для мероприятия.
    '''
    subevents = SubeventSerializer(many=True, read_only=True)
    # participants = serializers.StringRelatedField(many=True, read_only=True)
    participant_count = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'

    def get_participant_count(self, obj):
        return obj.registrations.count()

class EventRegistrationSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для регистрации на мероприятие.
    '''
    event = serializers.StringRelatedField(read_only=True)
    participant = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = EventRegistration
        fields = '__all__'

    def create(self, validated_data):
        current_count = EventRegistration.objects.filter(event=validated_data['event']).count()
        if current_count >= validated_data['event'].participant_limit:
            raise serializers.ValidationError('Достигнуто максимальное количество участников')
        return EventRegistration.objects.create(approved=True, **validated_data) # Stub for now
    
    def validate(self, attrs):
        event_id = self.context['view'].kwargs.get('event_id')
        user = self.context['request'].user
        if EventRegistration.objects.filter(event=event_id, participant=user).exists():
            raise serializers.ValidationError('Вы уже зарегистрированы на это мероприятие')
        return super().validate(attrs)
