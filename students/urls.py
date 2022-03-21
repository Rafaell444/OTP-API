from django.urls import path
from .views import UserList, UserDetail, Generate

urlpatterns = [
    path("", UserList.as_view()),
    path("<int:pk>", UserDetail.as_view()),
    # path("get/", Generate.as_view()),
    path("get/<int:pk>", Generate.as_view())
]