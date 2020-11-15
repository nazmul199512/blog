from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView
from .views import UserCreate, BlacklistTokenView

urlpatterns = [
    path("register/", UserCreate.as_view(), name="register"),
    path("logout/blacklist/", BlacklistTokenView.as_view(), name="blacklist"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]


