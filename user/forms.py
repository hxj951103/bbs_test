from django import forms

from user.models import User


class RegisterForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname', 'password', 'icon', 'sex', 'age']

    password2 = forms.CharField(required=True, max_length=128)

    def clean_password2(self):
        # 继承父类的clean,其中包含了以上定义的所有字段的值
        clean_data = super().clean()

        if len(clean_data['password']) < 8 :
            raise forms.ValidationError('密码长度过短')
        elif clean_data['password'] != clean_data['password2']:
            raise forms.ValidationError('两次密码不一致')




