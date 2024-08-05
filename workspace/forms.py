from django import forms

from django.contrib.auth.forms import AuthenticationForm

from pradact.models import Category, Pradact, Tag
from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password

# 2)
class PradactForm(forms.Form):
    name = forms.CharField(label='Название', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Название',
    }))
    image = forms.ImageField(label='Изображение', required=False, widget=forms.FileInput(attrs={
         'class': 'form-control',
    }))
    price = forms.DecimalField(label='Цена', max_digits=10, decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Цена',
        })
    )
    category = forms.ModelChoiceField(
        label='Категория', 
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    tags = forms.ModelMultipleChoiceField(
        label='Теги',
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '8'}))
    is_published = forms.BooleanField(label='Публичность', widget=forms.CheckboxInput(attrs={'id': 'news_is_pub'}))
# 3)
class PradactModelForm(forms.ModelForm):

    class Meta:
        model = Pradact
        fields = (
            'name',
            'description',
            'category',
            'tags',
            'image',
            'price',
            'is_published',
        )

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '8',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
            }),
            'tags': forms.CheckboxSelectMultiple(),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена',
            }),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }

# 1)

# class NewsFrom(forms.Form):

#     name = forms.CharField(label='Название', widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Название',
#     }))
#     image = forms.ImageField(label='Изображение', widget=forms.FileInput(attrs={
#          'class': 'form-control',
#     }))
#     category = forms.ModelChoiceField(
#         label='Категория', 
#         queryset=Category.objects.all(),
#         widget=forms.Select(attrs={'class': 'form-select'}),
#     )
#     tags = forms.ModelMultipleChoiceField(
#         label='Теги',
#         queryset=Tag.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#     )
#     content = forms.CharField(label='Контент', widget=forms.Textarea(attrs={'class': 'form-control', 'cols': '5'}))
#     description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'form-control', 'cols': '5'}))
#     price = forms.
#     is_published = forms.BooleanField(label='Публичность', widget=forms.CheckboxInput(attrs={'id': 'news_is_pub'}))
class LoginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={"autofocus": True, 'class': 'form-control'}), 
        label='Имя пользователя'
    )
    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'class': 'form-control'}),
    )
    

class RegisterForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True 
        self.fields['last_name'].required = True 
        self.fields['email'].required = True 


    password1 = forms.CharField(label='Придумайте пароль', validators=[validate_password], widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))



    class Meta:
        model = User
        # fields = '__all__'
        exclude = (
            'password', 
            'is_superuser', 
            'is_staff',
            'is_active',
            'user_permissions', 
            'groups', 
            'last_login', 
            'date_joined'
            )
        
        # labels = {
        #     'username': 'sdfsd'
        # }


        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    
    def clean(self):
       
        cleaned_data = super().clean()
        
        password1 = cleaned_data.pop('password1', None)
        password2 = cleaned_data.pop('password2', None)

        # errors = {}

        # if password1 is None:
        #     errors['password1'] = ['Обязательное поле.']

        # if password2 is None:
        #     errors['password2'] = ['Обязательное поле.']

        # if len(errors) > 0:
        #     raise forms.ValidationError(errors)

        if (password1 is not None and password2 is not None) and password1 != password2:
            raise forms.ValidationError({'password2': ['The passwords dont\'t match.']})

        
        password = make_password(password1)
        cleaned_data.setdefault('password', password)

        return cleaned_data