"""sih_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import admin_portal.views
import mobileapp.views as api
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,TokenVerifyView
)
from admin_portal.serializers import MyTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello/', admin_portal.views.HelloView.as_view(), name='hello'),
    # path('mobile/test/',mobileapp.views.hodLogin),
    # path('register/',mobileapp.views.HodRegisterView.as_view()),
    # path('orgLogin/',mobileapp.views.OrgLoginView.as_view()),
    path('api/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/hodAdd/',api.AdminHodCreate.as_view(), name="hodadd"),
    path('demo/',api.demoSerial, name="demo"),

]
