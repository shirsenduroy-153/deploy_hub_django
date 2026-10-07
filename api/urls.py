from django.urls import path
from .views import RootView, HelloView, HealthCheckView, InfoView

urlpatterns = [
    path('', RootView.as_view(), name='root'),
    path('api/hello', HelloView.as_view(), name='hello'),
    path('api/hello/', HelloView.as_view(), name='hello-slash'),
    path('api/health', HealthCheckView.as_view(), name='health'),
    path('api/health/', HealthCheckView.as_view(), name='health-slash'),
    path('api/info', InfoView.as_view(), name='info'),
    path('api/info/', InfoView.as_view(), name='info-slash'),
]
