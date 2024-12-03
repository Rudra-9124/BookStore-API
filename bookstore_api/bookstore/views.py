from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book, userProfile, Review
from .serializers import BookSerializer, ReviewSerializer, userProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend

class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'genre']

class ReviewViewset(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)
    
class UserProfileViewset(ModelViewSet):
    queryset = userProfile.objects.all()
    serializer_class = userProfileSerializer