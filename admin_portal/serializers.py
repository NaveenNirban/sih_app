import django.contrib.auth.password_validation as validators
from rest_framework import serializers
from admin_portal.forms import HodRegisterForm
from admin_portal.models import Hod, Parent,Teacher, Student
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class HodSerializer(serializers.ModelSerializer):
    #updatedById = MyUserSerializer()
    class Meta:
        model = Hod
        fields = ('id','email','first_name','last_name','username','type','date_joined','last_login')
        #fields = '__all__'
        #depth = 1

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id','email','first_name','last_name','username','type','date_joined','last_login')
        #fields = '__all__'
        #depth = 1

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','email','first_name','last_name','username','type','date_joined','last_login')
        #fields = '__all__'
        #depth = 1

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ('id','email','first_name','last_name','username','type','date_joined','last_login')
        #fields = '__all__'
        #depth = 1

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['type'] = user.type
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer