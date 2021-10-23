from rest_framework import serializers

from ..models import Works, Comments


class WorkSerializer(serializers.ModelSerializer):
    """
    Selection of the desired model and fields to be serialized in Json format.
    """

    class Meta:
        model = Works
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    """
    Selection of the desired model and fields to be serialized in Json format.
    """

    class Meta:
        model = Comments
        fields = '__all__'
