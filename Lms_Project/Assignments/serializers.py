from rest_framework import serializers
from .models import Assignment, Submission
from Users.models import Teacher

# Assignments serializer:


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'
        read_only_fields = ['teacher']  # Make the teacher field read-only

    def create(self, validated_data):
        # Get the logged-in user from the request context
        user = self.context['request'].user

        # Ensure the user is authenticated
        if not user.is_authenticated:
            raise serializers.ValidationError(
                "User must be authenticated to create an assignment.")

        # Get the teacher associated with the user
        try:
            teacher = Teacher.objects.get(user=user)
        except Teacher.DoesNotExist:
            raise serializers.ValidationError(
                "The logged-in user is not associated with a teacher.")

        # Add the teacher to the validated data
        validated_data['teacher'] = teacher

        # Create and return the assignment
        return super().create(validated_data)

# Submission Serializer:
class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'
    
