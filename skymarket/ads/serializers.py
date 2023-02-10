from rest_framework import serializers

from ads.models import Comment, Ad


class CommentSerializer(serializers.ModelSerializer):
    ad_id = serializers.IntegerField(read_only=True)
    author_first_name = serializers.ReadOnlyField(required=False, source="first_name")
    author_last_name = serializers.ReadOnlyField(required=False, source="last_name")
    author_image = serializers.ReadOnlyField(required=False, source="avatar_image")
    author = serializers.HiddenField(required=False, default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = [
            "pk",
            "text",
            "author_id",
            "created_at",
            "author_first_name",
            "author_last_name",
            "ad_id",
            "author_image",
            "author"
        ]


class AdSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(required=False)
    author_first_name = serializers.ReadOnlyField(required=False, source='author.first_name')
    author_last_name = serializers.ReadOnlyField(required=False, source='author.last_name')
    author_id = serializers.IntegerField(read_only=True)
    phone = serializers.CharField(required=False, source='author.phone')
    image = serializers.ReadOnlyField(required=False, source='image_url')

    class Meta:
        model = Ad
        fields = [
            "pk",
            "image",
            "title",
            "price",
            "phone",
            "description",
            "author_first_name",
            "author_last_name",
            "author_id"
        ]


class AdDetailSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(required=False)
    author_first_name = serializers.ReadOnlyField(required=False, source='author.first_name')
    author_last_name = serializers.ReadOnlyField(required=False, source='author.last_name')
    author_id = serializers.IntegerField(read_only=True)
    phone = serializers.CharField(required=False, source='author.phone')
    image = serializers.ReadOnlyField(required=False, source='image_url')

    class Meta:
        model = Ad
        fields = [
            "pk",
            "image",
            "title",
            "price",
            "phone",
            "description",
            "author_first_name",
            "author_last_name",
            "author_id"
        ]
