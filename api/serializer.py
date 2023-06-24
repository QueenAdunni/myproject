from rest_framework import serializers
from.models import Post,Description

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields= ('id','title','description', 'image_link', 'year', 'mins', 'ratings','video_link','bg_image_link','genere') 



class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Description
        fields= ('id','title','description', 'image_link') 