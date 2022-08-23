from django.contrib import admin
from .models import OrganizationMaster,User,HodMaster,TeachersMaster,Subjects,AdditionalClassTeachers,Parents,StandardMaster,StudentMaster,LearningMaterial,Circular,Homework,Attendance,Complaints,QRLibrary#CustomUserManager
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from admin_portal.forms import UserCreationForm

class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','username','mobile', 'password1', 'password2','type')}
        ),
    )
    # fields = ('type','username')

class OrganizationMasterAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.adminPassword = make_password(obj.adminPassword)
        super().save_model(request, obj, form, change)

class AdminHodMasterAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)

class TeachersMasterAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)

class ParentsAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)

class StudentsMasterAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)

# Register your models here.
admin.site.register(OrganizationMaster, OrganizationMasterAdmin)
admin.site.register(HodMaster, AdminHodMasterAdmin)
admin.site.register(TeachersMaster,TeachersMasterAdmin)
admin.site.register(Parents, ParentsAdmin)
admin.site.register(StudentMaster,StudentsMasterAdmin)

admin.site.register(Subjects)
admin.site.register(AdditionalClassTeachers)
admin.site.register(StandardMaster)
admin.site.register(LearningMaterial)
admin.site.register(Circular)
admin.site.register(Homework)
admin.site.register(Attendance)
admin.site.register(Complaints)
admin.site.register(QRLibrary)
admin.site.register(User, UserAdmin)