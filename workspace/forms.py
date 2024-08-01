from django import forms

from django.contrib.auth.forms import AuthenticationForm

from pradact.models import Category, Pradact, Tag
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