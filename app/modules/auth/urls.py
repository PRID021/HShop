from rest_framework.routers import DefaultRouter

from app.modules.auth.views import AuthViewSet

router = DefaultRouter()
router.register(r"", AuthViewSet, basename="auth")
