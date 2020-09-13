from rest_framework import serializers
from . import models


class ClubSerializer(serializers.ModelSerializer):
	created_at = serializers.ReadOnlyField()
	updated_at = serializers.ReadOnlyField()
	class Meta:
		model = models.Posts
		fields = '__all__'
