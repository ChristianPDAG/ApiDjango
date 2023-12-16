from django import forms
from django.forms import ModelForm
from .models import Usuarios
from django.contrib.auth.forms import UserCreationForm


class UserForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['email', 'nombre', 'apellido', 'celular', 'fecha_nacimiento', 'password']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'password': forms.PasswordInput(),
                }
        

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {'class':'form-control'}
        self.fields['apellido'].widget.attrs = {'class':'form-control'}
        self.fields['email'].widget.attrs = {'class':'form-control'}
        self.fields['fecha_nacimiento'].widget.attrs = {'class':'form-control'}
        self.fields['celular'].widget.attrs = {'class':'form-control'}
        self.fields['password'].widget.attrs = {'class':'form-control'}
        self.fields['email'].widget.attrs.update({'placeholder': 'example@mail.com'})

    
