import re
from unicodedata import name
from django.shortcuts import render
from mobileapp.models import HodMaster, OrganizationMaster, StandardMaster, StudentMaster, Subjects, TeachersMaster
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from mobileapp.models import Hod, Org, Student, Parent, Teacher, User, LearningMaterial
from mobileapp.forms import HodRegisterForm, StandardCreationForm, StudentForm, StudentMasterForm, TeacherRegisterForm
from mobileapp.serializers import ClassesSerializer, HodSerializer, HodMasterSerializer, LearningMaterialSerializer, LearningSerializer, OrganizationMasterSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from sih_app.enums import Role
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from django.conf import settings as django_settings
import uuid


def simple_upload(request):
    if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES['file']
        name = request.POST.get('name')
        file=open(os.path.join(django_settings.STATIC_ROOT,myfile.name))
        fs = FileSystemStorage()
        uploaded_file_url = fs.url(file.name)
        file.write(json)
        file.close()
    return uploaded_file_url

def handle_uploaded_file(file): 
    path = 'mobileapp/static/upload/'+str(uuid.uuid4())+file.name
    with open(path,'wb+') as destination:  
        for chunk in file.chunks():  
            destination.write(chunk) 
    return path

# Create your views here.


@csrf_exempt
def hodLogin(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    username = body['username']
    password = body['password']
    res = Hod.authenticate(username, password)
    return HttpResponse(res)
    # username = request.GET.get('username')
    # password = request.GET.get('password')

# @csrf_exempt
# def registerHod(request):
#     #print(request)
#     if request.method == "POST":
#         form = AdminRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             res = "sab bdiya h, ho gya h"
#         else:
#             res= "form not valid"
#         return HttpResponse(res)
#     else:
#         return HttpResponse("Method is not post")

# class HodRegisterView(APIView):
# 	# permission_classes = [IsAuthenticated]
# 	# authentication_classes = [SessionAuthentication, BasicAuthentication]
# 	def post(request):
# 		form = HodRegisterForm(request.POST)
# 		if form.is_valid():

# 			data = HodSerializer(user)
# 			# login(request, user)
# 			# messages.success(request, "Registration successful." )
# 			return JsonResponse({
# 				"success": True,
# 							"response": {
# 								"data": data.data,
# 								"message" :"" ,
# 							},
# 							"errors": []
# 			})
# 		return JsonResponse({
# 				"success": False,
# 							"response": {
# 								"data": [],
# 								"message" :"" ,
# 							},
# 							"errors": form.errors
# 			})
############### Login Obsolete methods ############


class OrgLoginView(APIView):
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        username = body['username']
        password = body['password']
        res = Org.authenticate(username, password)
        return JsonResponse(res)


class StudentLoginView(APIView):
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        username = body['username']
        password = body['password']
        res = Student.authenticate(username, password)
        return HttpResponse(res)


class ParentLoginView(APIView):
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        username = body['username']
        password = body['password']
        res = Parent.authenticate(username, password)
        return HttpResponse(res)


class HodLoginView(APIView):
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        username = body['username']
        password = body['password']
        res = Hod.authenticate(username, password)
        return HttpResponse(res)


class TeacherLoginView(APIView):
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        username = body['username']
        password = body['password']
        res = Hod.authenticate(username, password)
        return HttpResponse(res)

################## Working functions starts ##########

# Done
class AdminHodCreate(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        userType = request.user.type
        if userType == Role.Admin:
            # body_unicode = request.body.decode('utf-8')
            # body = json.loads(body_unicode)
            form = HodRegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                updatedBy = request.user.id
                orgMaster=None
                hodMasterUser=None
                try:
                    orgMaster = OrganizationMaster.objects.filter(
                        orgUser__id=request.user.id).first()
                    print(orgMaster)
                    
                    hodMasterUser = HodMaster(
                        org=orgMaster, hod=user, updatedBy=updatedBy)
                    print(hodMasterUser.org)
                    print(hodMasterUser)
                except Exception as e:
                    print(e)

                if hodMasterUser is not None and orgMaster is not None:

                    user.save()
                    hodMasterUser.save()
                    return JsonResponse({
                        "success": True,
                        "response": {
                            "data": "User created successfully",
                            "message": "",
                        },
                        "errors": []
                    }, safe=False)

                else:
                    data = HodMasterSerializer(user)
                    if orgMaster is None:
                        return JsonResponse({
                        "success": True,
                        "response": {
                            "data": [],
                            "message": "",
                        },
                        "errors": "No Organization master available"
                    })
                    return JsonResponse({
                        "success": True,
                        "response": {
                            "data": [],
                            "message": "",
                        },
                        "errors": "Error in saving data to HodMaster"
                    })

            return JsonResponse({
                "success": False,
                "response": {
                    "data": [],
                    "message": "",
                },
                "errors": form.errors
            })
        else:
            return JsonResponse({
                "success": False,
                "response": {
                    "data": [],
                    "message": "",
                },
                "errors": "You are not authorised to create HOD"
            })

# Done
class HodTeacherCreate(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        userType = request.user.type
        if userType == Role.HOD or userType == Role.Admin:
            # body_unicode = request.body.decode('utf-8')
            # body = json.loads(body_unicode)
            form = TeacherRegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                updatedBy = request.user.id

                teacherMasterUser=None
                hodMaster=None
                try:

                    hodMaster = HodMaster.objects.filter(
                        hod__id=request.user.id).first()
                    print(hodMaster)
                    
                    teacherMasterUser = TeachersMaster(
                        adminHod=hodMaster, teacherUsr=user, updatedBy=updatedBy)

                except Exception as e:

                    print(e)
                    return JsonResponse({
                        "success": False,
                        "response": {
                            "data": str(e),
                            "message": "",
                        },
                        "errors": []
                    }, safe=False)


                if teacherMasterUser is not None and hodMaster is not None:

                    user.save()
                    teacherMasterUser.save()
                    return JsonResponse({
                        "success": True,
                        "response": {
                            "data": "User created successfully",
                            "message": "",
                        },
                        "errors": []
                    }, safe=False)

                else:
                    #data = HodMasterSerializer(user)
                    if hodMaster is None:
                        return JsonResponse({
                        "success": True,
                        "response": {
                            "data": [],
                            "message": "",
                        },
                        "errors": "No Hod master available"
                    })
                    else:
                        return JsonResponse({
                            "success": True,
                            "response": {
                                "data": [],
                                "message": "",
                            },
                            "errors": "Error in saving data to HodMaster"
                        })

            return JsonResponse({
                "success": False,
                "response": {
                    "data": [],
                    "message": "",
                },
                "errors": form.errors
            })
        else:
            return JsonResponse({
                "success": False,
                "response": {
                    "data": [],
                    "message": "",
                },
                "errors": "You are not authorised to create HOD"
            })

# TeacherHodAdminAddStudent
class TeacherStudentCreate(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        userType = request.user.type
        if userType == Role.HOD or userType == Role.Admin or user == Role.Teacher:
            # body_unicode = request.body.decode('utf-8')
            # body = json.loads(body_unicode)
            form = StudentForm(request.POST)
            form2 = StudentMasterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                updatedBy = request.user.id
                try:
                    form2.faculty

                    hodMaster = HodMaster.objects.filter(
                        hod__id=request.user.id).first()
                    print(hodMaster)
                    
                    teacherMasterUser = TeachersMaster(
                        adminHod=hodMaster, teacherUsr=user, updatedBy=updatedBy)

                except Exception as e:

                    print(e)
                    return JsonResponse({
                        "success": False,
                        "response": {
                            "data": str(e),
                            "message": "",
                        },
                        "errors": []
                    }, safe=False)


                if teacherMasterUser is not None and hodMaster is not None:

                    user.save()
                    teacherMasterUser.save()
                    return JsonResponse({
                        "success": True,
                        "response": {
                            "data": "User created successfully",
                            "message": "",
                        },
                        "errors": []
                    }, safe=False)

                else:
                    #data = HodMasterSerializer(user)
                    if hodMaster is None:
                        return JsonResponse({
                        "success": True,
                        "response": {
                            "data": [],
                            "message": "",
                        },
                        "errors": "No Hod master available"
                    })
                    else:
                        return JsonResponse({
                            "success": True,
                            "response": {
                                "data": [],
                                "message": "",
                            },
                            "errors": "Error in saving data to HodMaster"
                        })

            return JsonResponse({
                "success": False,
                "response": {
                    "data": [],
                    "message": "",
                },
                "errors": form.errors
            })
        else:
            return JsonResponse({
                "success": False,
                "response": {
                    "data": [],
                    "message": "",
                },
                "errors": "You are not authorised to create HOD"
            })

# Add Classes
class TeacherAddContent(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        userType = request.user.type
        if (userType == Role.Teacher):
            if (request.FILES and request.POST.get('name')):
                fileName = request.POST.get('name')
                fileType = request.POST.get('type')
                fileUrl = handle_uploaded_file(request.FILES['file'])
                standard = request.POST.get('standardId')
                subject = request.POST.get('subjectId')
                contentObj = LearningMaterial()
                contentObj.url = fileUrl
                contentObj.name = fileName
                contentObj.fileType = fileType
                standardClassObj = StandardMaster.objects.filter(
                    id=standard).first()
                subjectObj = Subjects.objects.filter(id=subject).first()
                contentObj.subject = subjectObj
                contentObj.standard = standardClassObj
                contentObj.save()
                return JsonResponse({
                "success": True,
                "response": {
                    "data": [],
                    "message": "File uploaded successfully",
                },
                "errors": []
            })
            else:
                return JsonResponse({
                "success": False,
                "response": {
                    "data": [],
                    "message": "",
                },
                "errors": "Please add file,name,type,standardId,subjectId !"
            })




class StudentLearningMaterialClass(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        materialList = LearningMaterial.objects.all()
        data = LearningMaterialSerializer(materialList,many=True).data
        return JsonResponse({
                "success": True,
                "response": {
                    "data": data,
                    "message": "",
                },
                "errors": []
            })

class TeacherGetClasses(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        materialList = TeachersMaster.objects.all()
        for i in materialList:
            if i.teacherUsr.id==request.user.id:
                allClassses = StandardMaster.objects.filter(org=i.org)
                data = ClassesSerializer(allClassses,many=True).data
        return JsonResponse({
                "success": True,
                "response": {
                    "data": data,
                    "message": "",
                },
                "errors": []
            })

class StudentGetLearning(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data=[]
        materialList = StudentMaster.objects.all()
        for i in materialList:
            if i.student.id==request.user.id:
                material = LearningMaterial.objects.filter(standard=i.classDetails)
                data = LearningSerializer(material,many=True).data
        return JsonResponse({
                "success": True,
                "response": {
                    "data": data,
                    "message": "",
                },
                "errors": []
            })

class Standard(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        userType = request.user.id
        data = StandardMaster()
        data.updatedBy=userType
        #if userType == Role.Admin:
            # body_unicode = request.body.decode('utf-8')
            # body = json.loads(body_unicode)
        request.POST['updatedBy']="OIUYTRE"
        form = StandardCreationForm(request.POST)
        
        if form.is_valid():
            # user = form.save(commit=False)
            #print(form.data)
            #form.data['qwerty']="uytr"
            print(form.data)
            updatedBy = request.user.id
            return JsonResponse({
            "success": True,
            "response": {
                "data": "sab sahi",
                "message": "",
            },
            "errors": []
        })
        else:
            return JsonResponse({
                "success": False,
                "response": {
                    "data": [form.errors],
                    "message": "",
                },
                "errors": []
            })


@csrf_exempt
def demoSerial(request):
    data = HodMaster.objects.all().first()
    print(data)
    # print(data.type)
    # for i in data:
    # 	print(i.type)
    serialized = HodMasterSerializer(data)
    return JsonResponse(serialized.data, safe=False)