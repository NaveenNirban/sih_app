from dataclasses import field
import django.contrib.auth.password_validation as validators
from rest_framework import serializers
from admin_portal.forms import HodRegisterForm
from admin_portal.models import Hod, HodManager, HodMaster, LearningMaterial, Parent, StandardMaster,Teacher, Student,Org, OrganizationMaster
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from sih_app.enums import Enum, Role



class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Org
        fields = ('id','email','first_name','username','type')

class OrganizationMasterSerializer(serializers.ModelSerializer):
    orgUser = OrganizationSerializer()
    class Meta:
        model = OrganizationMaster
        fields = ('id',"orgUser")

class HodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hod
        fields = ('id','email','first_name')
        #fields = '__all__'
class HodMasterSerializer(serializers.ModelSerializer):
    #updatedById = MyUserSerializer()
    #hod = serializers.RelatedField(source="Hod",read_only =True)
    org  = OrganizationMasterSerializer()
    hod = HodSerializer()
    class Meta:
        model = HodMaster
        #fields = ('id','email','first_name','last_name','username','type','date_joined','last_login')
        fields = ('id','org','hod')
        
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
        if user.type == Role.Admin:
            token['type'] = user.type
            token['schoolName'] = user.first_name
            token['schoolImage'] = user.first_name
        if user.type == Role.HOD:
            token['type'] = user.type
            token['hodName'] = user.first_name
            token['schoolId'] = user.first_name
            token['email'] = user.email
            token['phone'] = user.mobile
        if user.type == Role.Teacher:
            token['type'] = user.type
            token['teacherName'] = user.first_name
            token['empId'] = str(user.id)
            token['email'] = user.email
            token['phone'] = user.mobile
        if user.type == Role.Student:
            token['type'] = user.type
            token['studentName'] = user.first_name
            token['schoolId'] = str(user.id)
            token['admissionNo'] = user.email
            token['phone'] = user.mobile
            token['kakshaId'] = str(user.id)
            token['fatherName'] = user.first_name

        
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class LearningMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningMaterial
        fields = ('id','url','name','fileType')

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StandardMaster
        fields = ('name','id')
        #fields = '__all__'
        #depth = 1
class LearningSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningMaterial
        fields = ('id','url','name','fileType')
        #fields = '__all__'
        #depth = 1