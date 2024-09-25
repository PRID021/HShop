from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from askservice.views import GroupViewSet, HelloWorldAPIView, UserViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"users", viewset=UserViewSet)
router.register(r"groups", viewset=GroupViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="Askservice API",
        default_version="v1",
        description="API documentation for AskService",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("hello/", HelloWorldAPIView.as_view(), name="hello"),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
