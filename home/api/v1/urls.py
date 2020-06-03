from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CustomTextViewSet,
    HomePageViewSet,
    R1ViewSet,
    R2ViewSet,
    R3ViewSet,
    R4ViewSet,
    TestViewSet,
)

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    HomePageViewSet,
    CustomTextViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("customtext", CustomTextViewSet)
router.register("homepage", HomePageViewSet)
router.register("test", TestViewSet)
router.register("r2", R2ViewSet)
router.register("r1", R1ViewSet)
router.register("r4", R4ViewSet)
router.register("r3", R3ViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
