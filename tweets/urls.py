from django.urls import path

from . import views

app_name = "tweets"

urlpatterns = [
    path("home/", views.Home_View, name="home"),
    path("create/", views.TweetCreateView.as_view(), name="create"),
    path("<str:pk>/", views.TweetDetail_View, name="detail"),
    path("<str:pk>/delete/", views.TweetDelete_View, name="delete"),
    # path('<int:pk>/like/', views.LikeView, name='like'),
    # path('<int:pk>/unlike/', views.UnlikeView, name='unlike'),
]
