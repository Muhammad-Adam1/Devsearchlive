from django.urls import path

from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # generate token for the user
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # refresh the token for the user, so that the user can stay logged in
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.getRoutes),
    path('projects/', views.getProjects),
    path('project/<str:pk>/', views.getProject),
    path('project/<str:pk>/vote/', views.projectVote),
]
