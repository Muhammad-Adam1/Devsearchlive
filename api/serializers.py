from rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import Profile

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    # nested serializers and serializers method fields 
    # they are over-riding the existing fields 
    owner = ProfileSerializer(many=False)
    # now the owner fields give us the Profile model data 
    tags = TagSerializer(many=True)
    # by doing this we can add the attribute in the json obj
    reviews = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = '__all__'
    
    def get_reviews(self, obj):
        # method that is for the json obj
        reviews = obj.review_set.all()
        # serialize all the reviews
        serializer = ReviewSerializer(reviews, many=True)
        # return the data of the serialized reviews to the reviews field in the ProjectSerializer
        return serializer.data