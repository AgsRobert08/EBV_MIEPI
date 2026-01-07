from django import forms
from .models import Inscrito


class InscritoForm(forms.ModelForm):

    class Meta:
        model = Inscrito
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True
            }),

            'genero': forms.RadioSelect(),

            'otra_denominacion': forms.CheckboxInput(attrs={
                'id': 'otra_denominacion'
            }),

            'denominacion': forms.TextInput(attrs={
                'id': 'denominacion'
            }),

            'zona': forms.Select(attrs={
                'id': 'zona'
            }),

            'subzona': forms.TextInput(attrs={
                'id': 'subzona'
            }),

            'grado': forms.Select(),

            'correo_electronico': forms.EmailInput(attrs={
                'required': True
            }),

            'telefono': forms.TextInput(attrs={
                'required': True
            }),

            # hidden (controlados por JS)
            'periodo': forms.HiddenInput(attrs={'id': 'periodo'}),
            'monto': forms.HiddenInput(attrs={'id': 'monto'}),
        }



class InscritoFormEdit(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = [
            'nombre',
            'genero',
            'otra_denominacion',
            'denominacion',
            'zona',
            'subzona',
            'telefono',
            'correo_electronico',
            'grado',
            'monto'
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'input'}),
            'zona': forms.TextInput(attrs={'class': 'input'}),
            'subzona': forms.TextInput(attrs={'class': 'input'}),
            'denominacion': forms.TextInput(attrs={'class': 'input'}),
            'telefono': forms.TextInput(attrs={'class': 'input'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'input'}),
            'grado': forms.TextInput(attrs={'class': 'input'}),
            'monto': forms.NumberInput(attrs={'class': 'input'}),
        }
