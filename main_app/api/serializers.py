from rest_framework import serializers

from ..models import Works, Comments


class WorkListSerializer(serializers.ModelSerializer):
    """
    Selection of the desired model and fields to be serialized in Json format.
    """

    class Meta:
        model = Works
        fields = '__all__'


class CommentsListSerializer(serializers.ModelSerializer):
    """
    Selection of the desired model and fields to be serialized in Json format.
    """

    class Meta:
        model = Comments
        fields = '__all__'


class WorkSerializer(serializers.ModelSerializer):
    """
    Selection of the desired model and fields to be serialized in Json format.
    """

    class Meta:
        model = Works
        fields = '__all__'  # All fields into the model Works


class CommentsSerializer(serializers.ModelSerializer):
    """
    Selection of the desired model and fields to be serialized in Json format.
    """

    class Meta:
        model = Comments  # The heir is model Comments.
        fields = '__all__'  # All fields into the model Comments
