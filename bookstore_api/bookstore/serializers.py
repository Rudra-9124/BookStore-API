from rest_framework import serializers
from .models import Book, userProfile, Review
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class userProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = userProfile
        fields = ['user', 'bio', 'profile_picture']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['book', 'user', 'rating', 'content']
        