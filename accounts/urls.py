from django.urls import include, path

from .views import ProfileListAPIView

app_name = 'news'


urlpatterns = [
      path('profiles/', ProfileListAPIView.as_view()),
]
