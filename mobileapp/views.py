from django.shortcuts import render
from admin_portal.models import HodMaster, OrganizationMaster
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from admin_portal.models import Hod,Org,Student,Parent,Teacher
from admin_portal.forms import HodRegisterForm
from admin_portal.serializers import HodSerializer, HodMasterSerializer, OrganizationMasterSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from sih_app.enums import Role



# Create your views here.
@csrf_exempt
def hodLogin(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    username = body['username']
    password = body['password']
    res = Hod.authenticate(username,password)
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
	def post(self,request):
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		username = body['username']
		password = body['password']
		res = Org.authenticate(username,password)
		return JsonResponse(res)

class StudentLoginView(APIView):
	def post(self,request):
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		username = body['username']
		password = body['password']
		res = Student.authenticate(username,password)
		return HttpResponse(res)
	
class ParentLoginView(APIView):
	def post(self,request):
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		username = body['username']
		password = body['password']
		res = Parent.authenticate(username,password)
		return HttpResponse(res)

class HodLoginView(APIView):
	def post(self,request):
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		username = body['username']
		password = body['password']
		res = Hod.authenticate(username,password)
		return HttpResponse(res)

class TeacherLoginView(APIView):
	def post(self,request):
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		username = body['username']
		password = body['password']
		res = Hod.authenticate(username,password)
		return HttpResponse(res)

################## Working functions starts ##########
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
				#print(type(user))
				
				try:
					orgMaster = OrganizationMaster.objects.filter(orgUser__id=request.user.id).first()
					hodMasterUser = HodMaster(org=orgMaster,hod=user,updatedBy=updatedBy)
					user.save()
					#hodMasterUser.save()
					print(hodMasterUser.org)
				except Exception as e:
					print(e)
				
				
				#userMaster.org = OrganizationMaster.objects.filter(orgUser__id=request.user.id).first()
				
				#print(hodMasterUser)
				if hodMasterUser is not None:
		
					data = HodMasterSerializer(user)
					print(data.data)

				# login(request, user)
				# messages.success(request, "Registration successful." )
					return JsonResponse({
						"success": True,
								"response": {
									"data": data.data,
									"message" :"" ,   
								},
								"errors": []
						},safe=False)
				else:
					data = HodMasterSerializer(user)
				# login(request, user)
				# messages.success(request, "Registration successful." )
					return JsonResponse({
					"success": True,
								"response": {
									"data": [],
									"message" :"" ,   
								},
								"errors": "Error in saving data to HodMaster"
				})
				
			return JsonResponse({
					"success": False,
								"response": {
									"data": [],
									"message" :"" ,   
								},
								"errors": form.errors
				})
		else:
			return JsonResponse({
					"success": False,
								"response": {
									"data": [],
									"message" :"" ,   
								},
								"errors": "You are not authorised to create HOD"
				})

@csrf_exempt	
def demoSerial(request):
	data = HodMaster.objects.all().first()
	print(data)
	# print(data.type)
	# for i in data:
	# 	print(i.type)
	serialized = HodMasterSerializer(data)
	return JsonResponse(serialized.data,safe=False)