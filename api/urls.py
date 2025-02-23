from django.urls import URLPattern, path

from api.views import User_Subscribe

urlpatterns: list[URLPattern] = [
    path("subscribe/", User_Subscribe.as_view(), name="User_Subscribe"),
]
