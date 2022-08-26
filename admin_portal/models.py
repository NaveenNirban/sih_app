from audioop import reverse
from calendar import c
from pyexpat import model
from weakref import proxy

from rest_framework.authtoken.models import Token
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, UserManager, BaseUserManager
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import check_password, make_password
from sih_app.enums import Role



#   ORGANIZATION( App Manager ) --> HOD --> TEACHER --> STANDARD
#   SUBJECTS --> ADDITIONAL TEACHERS
#
#
#


class User(AbstractUser):
    objects = UserManager()

    class Types(models.TextChoices):
        ORGANIZATION = Role.Admin, "Organization"
        HOD = Role.HOD, "Hod"
        TEACHER = Role.Teacher, "Teacher"
        STUDENT = Role.Student, "Student"
        PARENT = Role.Parent, "Parent"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(_("Email"), max_length=255, unique=True,blank=True,null=True)
    mobile = models.IntegerField(
        _("Mobile"), max_length=12, unique=True, null=True)
    type = models.CharField(_("Type"), max_length=50, choices=Types.choices)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

class TeacherManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.TEACHER)


class Teacher(User):
    #objects = TeacherManager()

    def save(self, *args, **kwargs):
        if not self.type:
            self.type = User.Types.TEACHER
        return super().save(*args, **kwargs)

    def authenticate(username, password):
        user = Teacher.objects.filter(username=username).first()
        res = ""
        if user is not None:
            if (check_password(password, user.password)):
                #data = HodSerializer(user)
                try:
                    token = Token.objects.get(user_id=user.id)

                except Token.DoesNotExist:
                    token = Token.objects.create(user=user)
                res = {"success": True,
                       "response": {
                           "data": {"token": token.key},
                           "message": "Login Successful",
                       },
                       "errors": []
                       }
            else:
                res = {
                    "success": False,
                    "response": {
                        "data": [],
                        "message": "",
                    },
                    "errors": "Wrong password"
                }
        else:
            res = {
                "success": False,
                "response": {
                    "data": [],
                    "message": "",
                },
                "errors": "User does not exist"
            }
        return res

    class Meta:
        proxy = True


class Hod(User):
    #objects = HodManager()

    def save(self, *args, **kwargs):
        if not self.type:
            self.type = User.Types.HOD
        return super().save(*args, **kwargs)

    def authenticate(username, password):
        user = Hod.objects.filter(username=username).first()
        res = ""
        if user is not None:
            if (check_password(password, user.password)):
                #data = HodSerializer(user)
                try:
                    token = Token.objects.get(user_id=user.id)

                except Token.DoesNotExist:
                    token = Token.objects.create(user=user)
                res = {"success": True,
                       "response": {
                           "data": {"token": token.key},
                           "message": "Login Successful",
                       },
                       "errors": []
                       }
            else:
                res = {
                    "success": False,
                    "response": {
                        "data": [],
                        "message": "",
                    },
                    "errors": "Wrong password"
                }
        else:
            res = {
                "success": False,
                "response": {
                    "data": [],
                    "message": "",
                },
                "errors": "User does not exist"
            }
        return res

    # def get_user(self, user_id):
    #     try:
    #         return User.objects.get(pk=user_id)
    #     except User.DoesNotExist:
    #         return None

    class Meta:
        proxy = True


class Org(User):
    def save(self, *args, **kwargs):
        if not self.type:
            self.type = User.Types.ORGANIZATION
        return super().save(*args, **kwargs)

    def authenticate(username, password):

        user = Org.objects.filter(username=username).first()
        res = ""
        if user is not None:
            if (check_password(password, user.password)):
                #data = HodSerializer(user)
                try:
                    token = Token.objects.get(user_id=user.id)

                except Token.DoesNotExist:
                    token = Token.objects.create(user=user)
                res = {"success": True,
                       "response": {
                           "data": {"token": token.key},
                           "message": "Login Successful",
                       },
                       "errors": []
                       }
            else:
                res = {
                    "success": False,
                    "response": {
                        "data": [],
                        "message": "",
                    },
                    "errors": "Wrong password"
                }
        else:
            res = {
                "success": False,
                "response": {
                    "data": [],
                    "message": "",
                },
                "errors": "User does not exist"
            }
        return res

    class Meta:
        proxy = True

class OrganizationManager(models.Manager):
    # def create_user(self, email, password, **extra_fields):
    #     """
    #     Create and save a User with the given email and password.
    #     """
    #     if not email:
    #         raise ValueError(_('The Email must be set'))
    #     email = self.normalize_email(email)
    #     user = self.model(email=email, **extra_fields)
    #     user.set_password(password)
    #     user.save()
    #     return user
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.ORGANIZATION)

class HodManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.HOD)


class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.STUDENT)

class ParentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.PARENT)

###########################################





class Student(User):
    objects = StudentManager()

    def save(self, *args, **kwargs):
        if not self.type:
            self.type = User.Types.STUDENT
        return super().save(*args, **kwargs)

    def authenticate(username, password):
        user = Student.objects.filter(username=username).first()
        res = ""
        if user is not None:
            if (check_password(password, user.password)):
                #data = HodSerializer(user)
                try:
                    token = Token.objects.get(user_id=user.id)

                except Token.DoesNotExist:
                    token = Token.objects.create(user=user)
                res = {"success": True,
                       "response": {
                           "data": {"token": token.key},
                           "message": "Login Successful",
                       },
                       "errors": []
                       }
            else:
                res = {
                    "success": False,
                    "response": {
                        "data": [],
                        "message": "",
                    },
                    "errors": "Wrong password"
                }
        else:
            res = {
                "success": False,
                "response": {
                    "data": [],
                    "message": "",
                },
                "errors": "User does not exist"
            }
        return res

    class Meta:
        proxy = True

class Parent(User):
    objects = ParentManager()

    def save(self, *args, **kwargs):
        if not self.type:
            self.type = User.Types.PARENT
        return super().save(*args, **kwargs)

    def authenticate(username, password):
        user = Parent.objects.filter(username=username).first()
        res = ""
        if user is not None:
            if (check_password(password, user.password)):
                #data = HodSerializer(user)
                try:
                    token = Token.objects.get(user_id=user.id)
                except Token.DoesNotExist:
                    token = Token.objects.create(user=user)
                res = {"success": True,
                       "response": {
                           "data": {"token": token.key},
                           "message": "Login Successful",
                       },
                       "errors": []
                       }
            else:
                res = {
                    "success": False,
                    "response": {
                        "data": [],
                        "message": "",
                    },
                    "errors": "Wrong password"
                }
        else:
            res = {
                "success": False,
                "response": {
                    "data": [],
                    "message": "",
                },
                "errors": "User does not exist"
            }
        return res

    class Meta:
        proxy = True


class OrganizationMaster(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.CharField(max_length=255)
    orgUser = models.ForeignKey(
        Org, on_delete=models.CASCADE, default=None,null=True, blank=True,related_name='orgUser')
    siteUrl = models.URLField(null=True)
    image = models.URLField(null=True)
    isActive = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    updatedBy = models.CharField(max_length=40, null=True, blank=True)

class HodMaster(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    org = models.ForeignKey(
        OrganizationMaster, on_delete=models.CASCADE,related_name="org")
    hod = models.ForeignKey(
        Hod, on_delete=models.CASCADE,related_name="hod")
    isActive = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    updatedBy = models.CharField(max_length=40, null=True, blank=True)


class TeachersMaster(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    org = models.ForeignKey(
        OrganizationMaster, on_delete=models.CASCADE, blank=True)
    adminHod = models.ForeignKey(
        HodMaster, on_delete=models.CASCADE, blank=True)
    empNo = models.CharField(max_length=20,null=True,blank=True)
    teacherUsr = models.ForeignKey(Teacher,on_delete=models.CASCADE, blank=True)
    dob = models.DateField()
    doj = models.DateField()
    image = models.CharField(max_length=255)
    isActive = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    updatedBy = models.CharField(max_length=40, null=True, blank=True)


class Subjects(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    isActive = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    updatedBy = models.CharField(max_length=40, null=True, blank=True)


class AdditionalClassTeachers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, blank=True)
    # standard = models.ForeignKey(StandardMaster ,on_delete=models.CASCADE,blank=True)
    teacher = models.ForeignKey(
        TeachersMaster, on_delete=models.CASCADE, blank=True)
    isActive = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    updatedBy = models.CharField(max_length=40, null=True, blank=True)


class Parents(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    isActive = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True, blank=True)
    updatedBy = models.CharField(max_length=40, null=True, blank=True)


class StandardMaster(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    org = models.ForeignKey(
        OrganizationMaster, on_delete=models.CASCADE, blank=True)
    classTeacher = models.ForeignKey(
        TeachersMaster, on_delete=models.CASCADE, blank=True)
    isActive = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    updatedBy = models.CharField(max_length=40, null=True, blank=True)


class StudentMaster(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    orgId = models.ForeignKey(
        OrganizationMaster, on_delete=models.CASCADE, blank=True)
    hod = models.ForeignKey(HodMaster, on_delete=models.CASCADE, blank=True)
    faculty = models.ForeignKey(
        AdditionalClassTeachers, on_delete=models.CASCADE, blank=True)
    classDetails = models.ForeignKey(
        StandardMaster, on_delete=models.CASCADE, blank=True)
    parents = models.ForeignKey(Parents, on_delete=models.CASCADE, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, default="")
    
    dob = models.DateField(null=True)
    admissionNo = models.CharField(max_length=255, unique=True)
    isActive = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    updatedBy = models.CharField(max_length=40, null=True, blank=True)


class LearningMaterial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField(max_length=255)
    name = models.CharField(max_length=255)
    standard = models.ForeignKey(
        StandardMaster, on_delete=models.CASCADE, blank=True)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, blank=True)
    fileType = models.CharField(max_length=255)
    isActive = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    updatedBy = models.CharField(max_length=40, null=True, blank=True)


class Circular(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField()
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True, max_length=1000)
    isFor = models.IntegerField()
    standard = models.ForeignKey(StandardMaster, on_delete=models.CASCADE, blank=True)
    isActive = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    updatedBy = models.CharField(max_length=40, null=True, blank=True)


class Homework(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    isActive = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    url = models.URLField(null=True)
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    standard = models.ForeignKey(StandardMaster, on_delete=models.CASCADE, blank=True)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, blank=True)
    assignedBy = models.ForeignKey(
        TeachersMaster, on_delete=models.CASCADE, blank=True)
    forDate = models.DateField()
    updatedBy = models.CharField(max_length=40, null=True, blank=True)


class Attendance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    isActive = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(
        StudentMaster, on_delete=models.CASCADE, blank=True)
    teacher = models.ForeignKey(
        TeachersMaster, on_delete=models.CASCADE, blank=True)
    standard = models.ForeignKey(
        StandardMaster, on_delete=models.CASCADE, blank=True)
    date = models.DateTimeField()
    title = models.CharField(max_length=255)
    updatedBy = models.CharField(max_length=40, null=True, blank=True)


class Complaints(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    isActive = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    toHod = models.BooleanField(default=False)
    toTeacher = models.BooleanField(default=True)
    toMgmt = models.BooleanField(default=False)
    status = models.IntegerField(default=0)
    student = models.ForeignKey(
        StudentMaster, on_delete=models.CASCADE, blank=True)
    teacher = models.ForeignKey(
        TeachersMaster, on_delete=models.CASCADE, blank=True)
    hod = models.ForeignKey(HodMaster, on_delete=models.CASCADE, blank=True)
    org = models.ForeignKey(
        OrganizationMaster, on_delete=models.CASCADE, blank=True)
    complaintContent = models.TextField()
    updatedBy = models.CharField(max_length=40, null=True, blank=True)


class QRLibrary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    isActive = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    # Storing owner id into string as it may be of teacher or student
    owner = models.CharField(max_length=255)
    content = models.TextField()
    standard = models.ForeignKey(
        StandardMaster, on_delete=models.CASCADE, blank=True)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, blank=True)
    updatedBy = models.CharField(max_length=40, null=True, blank=True)
# class CustomUserManager(UserManager):
#     def create_user(self, email, password=None):
#         """
#         Creates and saves a User with the given email, date of
#         birth and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(
#             email=self.normalize_email(email),
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, date_of_birth, password=None):
#         """
#         Creates and saves a superuser with the given email, date of
#         birth and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#             date_of_birth=date_of_birth,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user



###########################################



