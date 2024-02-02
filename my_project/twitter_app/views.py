# twitter_app/views.py
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser as User, Tweet
from .serializers import UserSerializer, TweetSerializer

class CreateUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        try:
            user = User.objects.create_user(username=email, email=email)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response({'message': 'User with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)


class CreateTweetAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        body = request.data.get('body')
        user = User.objects.get(id=user_id)
        tweet = Tweet.objects.create(user=user, body=body)
        serializer = TweetSerializer(tweet)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

class GetTweetFeedAPIView(APIView):
    def get(self, request, user_id, *args, **kwargs):
        user = User.objects.get(id=user_id)
        tweets = Tweet.objects.filter(user=user)
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
