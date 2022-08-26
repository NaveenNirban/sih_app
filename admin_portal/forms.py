from django.contrib.auth.forms import UserCreationForm
from django import forms
from admin_portal.models import Hod, HodMaster, Teacher, User

# class AdminRegisterForm(UserCreationForm):
#     #email = forms.EmailField(label = "Email")
#     username = forms.CharField(label = "Username")
#     password = forms.CharField(label= "Password")
#     class Meta:
#         model = Admin
#         fields = ("password","username" )
#     def save(self, commit=True):
# 		user = super(AdminRegisterForm,self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		if commit:
# 			user.save()
# 		return user

class HodRegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = Hod
		fields = ("username", "email", "mobile", "first_name","password1","password2")

	def save(self, commit=True):
		user = super(HodRegisterForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class TeacherRegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = Teacher
		fields = ("username", "email", "mobile", "first_name","password1","password2")

	def save(self, commit=True):
		user = super(TeacherRegisterForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class HodMasterRegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = HodMaster
		fields = ("org", "updatedBy", "isActive")

	def save(self, commit=True):
		user = super(HodMasterRegisterForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

# Admin required data