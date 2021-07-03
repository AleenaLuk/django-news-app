from django.urls import include, path

from .views import ProfileListAPIView, ProfileDetailAPIView

app_name = 'news'


urlpatterns = [
    path('profiles/user/', ProfileDetailAPIView.as_view()),
    path('profiles/', ProfileListAPIView.as_view()),
]
