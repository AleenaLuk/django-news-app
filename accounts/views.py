from rest_framework import generics
from django.shortcuts import get_object_or_404

from .models import Profile
from .serializers import ProfileSerializer

class ProfileListAPIView(generics.ListCreateAPIView): # a get records request and a post request
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Create your views here.

class ProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView): # get a specific record, edit a record, or delete a record
    queryset = Profile.objects.all();
    serializer_class = ProfileSerializer

    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)
