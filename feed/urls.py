from django.urls import path
from .views import HomePageView, DetailPageView, FormPageView

app_name = "feed"

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("detail/<int:pk>/", DetailPageView.as_view(), name="detail"),
    path("post/", FormPageView.as_view(), name="post")
]