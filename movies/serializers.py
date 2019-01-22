from rest_framework import serializers
from models import *

class MovieSerializer(serializers.ModelSerializer):

    genre = serializers.StringRelatedField(many=True)
    director = serializers.StringRelatedField(many=False)

    class Meta:

        model = Movie
        fields = "__all__"