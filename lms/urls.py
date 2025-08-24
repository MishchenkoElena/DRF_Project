from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.urls import app_name

from lms.views import (
    CourseViewSet,
    LessonListApiView,
    LessonCreateApiView,
    LessonUpdateApiView,
    LessonRetrieveApiView,
    LessonDestroyApiView,
)

from lms.apps import LmsConfig

app_name = LmsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListApiView.as_view(), name="lessons_list"),
    path("lessons/<int:pk>/", LessonRetrieveApiView.as_view(), name="lessons_retrieve"),
    path("lessons/create/", LessonCreateApiView.as_view(), name="lessons_create"),
    path(
        "lessons/<int:pk>/update/", LessonUpdateApiView.as_view(), name="lessons_update"
    ),
    path(
        "lessons/<int:pk>/destroy/",
        LessonDestroyApiView.as_view(),
        name="lessons_destroy",
    ),
]

urlpatterns += router.urls
