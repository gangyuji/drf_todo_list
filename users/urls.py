from django.urls import path, include
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', views.UserView.as_view(), name='user_view'),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('<int:user_id>/', views.ToDoListUserView.as_view(), name='todolist_user'),
]
