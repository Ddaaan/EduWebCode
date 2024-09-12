from django import forms

class LoginForm(forms.Form):
    school_id = forms.CharField(label="아이디", max_length=100)
    school_pw = forms.CharField(label="비밀번호", widget=forms.PasswordInput)
