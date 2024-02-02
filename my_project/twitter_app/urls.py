# twitter_app/urls.py

from django.urls import path
from .views import CreateUserAPIView, CreateTweetAPIView, GetTweetFeedAPIView

urlpatterns = [
    path('user/', CreateUserAPIView.as_view(), name='create_user'),
    path('tweet/', CreateTweetAPIView.as_view(), name='create_tweet'),
    path('user/<str:user_id>/feed/', GetTweetFeedAPIView.as_view(), name='get_tweet_feed'),
]
