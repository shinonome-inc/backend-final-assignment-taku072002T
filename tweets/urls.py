from django.urls import path

from . import views

app_name = "tweets"

urlpatterns = [
    path("home/", views.HomeView, name="home"),
    path("create/", views.TweetCreationView.as_view(), name="create"),
    path("<str:pk>/", views.TweetDetailView, name="detail"),
    path("<str:pk>/delete/", views.TweetDeleteView, name="delete"),
    path("<str:pk>/deletes/", views.TweetDeletesView, name="deletes"),
    # path('<int:pk>/like/', views.LikeView, name='like'),
    # path('<int:pk>/unlike/', views.UnlikeView, name='unlike'),
]
