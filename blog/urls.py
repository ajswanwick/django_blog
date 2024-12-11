from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
     path("", views.event_detail, name="event_detail"),
     path('<slug:slug>/', views.post_detail, name='post_detail'),
]