from rest_framework import serializers
from .models import LiveMeeting

class MeetingSerialzier(serializers.ModelSerializer):
    class Meta:
        model = LiveMeeting
        fields = '__all__'

        