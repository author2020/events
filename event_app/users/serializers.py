from datetime import datetime

from djoser.serializers import UserSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User, Specialization


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ('id', 'name')

class CustomUserSerializer(UserSerializer):
    email = serializers.EmailField(required=True,
                                   validators=[UniqueValidator(queryset=User.objects.all())])
    profile_full = serializers.SerializerMethodField()
    specialization = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Specialization.objects.all(), required=False)

    class Meta(UserSerializer.Meta):
        fields = ('id', 'email', 'first_name', 'last_name',
                  'role', 'phone', 'employer', 'occupation',
                  'experience', 'specialization', 'preferred_format',
                  'consent_personal_data_processing',
                  'consent_personal_data_date',
                  'consent_vacancy_data_processing',
                  'consent_vacancy_data_date',
                  'consent_random_coffee', 'profile_full')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('id', 'role',
                            'consent_personal_data_date',
                            'consent_vacancy_data_date',
                            'profile_full')
        model = User

    def get_profile_full(self, obj):
        return obj.profile_full
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
            del validated_data['password']
        if 'consent_personal_data_processing' in validated_data:
            instance.consent_personal_data_date = datetime.now()
        if 'consent_vacancy_data_processing' in validated_data:
            instance.consent_vacancy_data_date = datetime.now()
        if 'specialization' in validated_data:
            instance.specialization.clear()
            instance.specialization.set(validated_data.pop('specialization'))
        return super().update(instance, validated_data)
    
    def create(self, validated_data):
        if 'consent_personal_data_processing' in validated_data:
            validated_data['consent_personal_data_date'] = datetime.now()
        if 'consent_vacancy_data_processing' in validated_data:
            validated_data['consent_vacancy_data_date'] = datetime.now()
        user = User.objects.create_user(**validated_data)
        if 'specialization' in validated_data:
            user.specialization.set(validated_data.pop('specialization'))
        return user
    
