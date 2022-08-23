from django.shortcuts import render
from admin_portal.models import HodMaster
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from admin_portal.models import Hod,Org,Student,Parent,Teacher
from admin_portal.forms import HodRegisterForm
from admin_portal.serializers import HodSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


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

class HodRegisterView(APIView):
	# permission_classes = [IsAuthenticated]
	# authentication_classes = [SessionAuthentication, BasicAuthentication]
	def post(request):
		form = HodRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			data = HodSerializer(user)
			# login(request, user)
			# messages.success(request, "Registration successful." )
			return JsonResponse({
				"success": True,
							"response": {
								"data": data.data,
								"message" :"" ,   
							},
							"errors": []
			})
		return JsonResponse({
				"success": False,
							"response": {
								"data": [],
								"message" :"" ,   
							},
							"errors": form.errors
			})

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