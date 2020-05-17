from django import forms
from .models import Customuser
from django.forms import ModelForm

"""class BaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for bound_field in self:
            if hasattr(bound_field, "field") and bound_field.field.required:
                bound_field.field.widget.attrs["required"] = "required"
                
class UserForm(BaseForm):
    class Meta:
        model = Customuser
        fields = [] """

class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email address', 'class':'form-control', 'id':'inputUsername'}), label="Username")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':'form-control', 'id':'inputPassword'}))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customuser
        fields = ['first_name', 'last_name', 'middle_name', 'gender', 'email', 'phonenumber', 'date_of_birth', 'religion', 'nok1_name',
                  'nok1_phone', 'nok1_relationship', 'admission_no', 'state_of_origin',
                  'lga', 'resident_type', 'house_address', 'prev_school', 'passport' ]
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        req_fields = ['first_name', 'last_name', 'gender', 'email', 'phonenumber', 'date_of_birth',
                  'religion', 'nok1_name', 'nok1_phone', 'nok1_relationship', 'state_of_origin',
                  'lga', 'resident_type', 'house_address', 'passport']
        for field in req_fields:
            self.fields[field].required = True


class DisabledForm(forms.ModelForm):
    class Meta:
        model = Customuser
        fields = ['first_name', 'last_name', 'middle_name', 'gender', 'email', 'phonenumber', 'date_of_birth', 'religion', 'nok1_name',
                  'nok1_phone', 'nok1_relationship', 'admission_no', 'state_of_origin',
                  'lga', 'resident_type', 'house_address',  'prev_school', 'passport' ]
    def __init__(self, *args, **kwargs):
        super(DisabledForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].disabled = True
        self.fields['first_name'].required = True
        disabled_fields = ['first_name', 'last_name', 'middle_name', 'gender', 'date_of_birth', 'admission_no', 'state_of_origin',
                  'lga', 'resident_type' ]


        req_fields = ['first_name', 'last_name' , 'gender', 'email', 'phonenumber', 'date_of_birth',
                  'religion', 'nok1_name', 'nok1_phone', 'nok1_relationship', 'state_of_origin',
                  'lga', 'resident_type', 'house_address']
        for field in req_fields:
            self.fields[field].required = True

        for field in disabled_fields:
            self.fields[field].disabled = True
            self.fields[field].required = False
        #self.fields['last_name'].disabled = True


