# from rest_framework import serializers
# from.models import Rating


# class RatingSerializer(serializers.ModelSerializer):
# rater = serializers.SerializerMethodField(read_omly=True)
# agent = serializers.SerializerMethodField(read_onky=True)

# class Meta:
# model = Rating
# execlude = ["update_at", "pkid"]

# def get_rater(self, obj):
# return obj.rater.username

# def get_agent(self, obj):
# return obj.agent.username