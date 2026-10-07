import socket
import sys
from datetime import datetime, timezone
import django
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def get_host_details():
    try:
        hostname = socket.gethostname()
        host_address = socket.gethostbyname(hostname)
    except Exception:
        hostname = "unknown"
        host_address = "127.0.0.1"
    return hostname, host_address

class RootView(APIView):
    def get(self, request):
        hostname, host_address = get_host_details()
        return Response({
            "status": "SUCCESS",
            "message": "Hello Deployment Test User! Django application is successfully deployed and running!",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "hostname": hostname,
            "hostAddress": host_address,
            "framework": f"Django {django.get_version()}",
            "pythonVersion": sys.version.split()[0]
        }, status=status.HTTP_200_OK)

class HelloView(APIView):
    def get(self, request):
        name = request.query_params.get("name", "World")
        hostname, host_address = get_host_details()
        return Response({
            "status": "SUCCESS",
            "message": f"Hello {name}! Django application is successfully deployed and running!",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "hostname": hostname,
            "hostAddress": host_address,
            "framework": f"Django {django.get_version()}",
            "pythonVersion": sys.version.split()[0]
        }, status=status.HTTP_200_OK)

class HealthCheckView(APIView):
    def get(self, request):
        return Response({
            "status": "UP",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "service": "deploy_hub_django"
        }, status=status.HTTP_200_OK)

class InfoView(APIView):
    def get(self, request):
        hostname, host_address = get_host_details()
        return Response({
            "appName": "deploy_hub_django",
            "version": "1.0.0",
            "framework": f"Django {django.get_version()}",
            "pythonVersion": sys.version.split()[0],
            "hostname": hostname,
            "hostAddress": host_address,
            "endpoints": [
                {"method": "GET", "path": "/", "description": "Root deployment sanity check"},
                {"method": "GET", "path": "/api/hello?name=John", "description": "Greeting endpoint"},
                {"method": "GET", "path": "/api/health", "description": "Health status probe"},
                {"method": "GET", "path": "/api/info", "description": "Application info & metadata"}
            ]
        }, status=status.HTTP_200_OK)
