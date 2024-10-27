from django import forms

class LoginForm(forms.Form):
    school_id = forms.CharField(label="아이디", max_length=100)
    school_pw = forms.CharField(label="비밀번호", widget=forms.PasswordInput)


class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '현재 비밀번호'}), label='현재 비밀번호')
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '새 비밀번호'}), label='새 비밀번호')
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '새 비밀번호 확인'}), label='새 비밀번호 확인')