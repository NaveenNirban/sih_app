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
import mobileapp.views
import mobileapp.views as api
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,TokenVerifyView
)
from mobileapp.serializers import MyTokenObtainPairView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='School App API')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello/', admin_portal.views.HelloView.as_view(), name='hello'),
    # path('mobile/test/',mobileapp.views.hodLogin),
    # path('register/',mobileapp.views.HodRegisterView.as_view()),
    # path('orgLogin/',mobileapp.views.OrgLoginView.as_view()),
    #path('swagger/',schema_view),
    path('api/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/hodAdd/',api.AdminHodCreate.as_view(), name="hodadd"),
    path('api/teacherAdd/',api.HodTeacherCreate.as_view(), name="teacheradd"),
    path('api/addStudyMaterial/',api.TeacherAddContent.as_view(), name="addStudyMaterial"),
    path('api/getLearningMaterial/',api.StudentLearningMaterialClass.as_view(), name="getLearningMaterial"),
    path('api/createPlaylist/',api.HodTeacherCreate.as_view(), name="createPlaylist"),
    path('api/getClasses/',api.TeacherGetClasses.as_view(), name="getClasses"),
    path('api/getLearning/',api.StudentGetLearning.as_view(), name="getLearning"),
    path('api/standard/',api.Standard.as_view(), name="standard"),

    path('demo/',api.demoSerial, name="demo"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
