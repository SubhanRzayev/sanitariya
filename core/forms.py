from django import forms
from django.db.models import fields
from django.forms import widgets

from core.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = {
            'name',
            'email',
            'subject',
            'message',
        }

        widgets = {
            'name':forms.TextInput(attrs={
                        'class': 'form-control',
                        'placeholder':'Your name',
                         
                    }),

            'email':forms.EmailInput(attrs={
                        'class':'form-control',
                        'placeholder':'Your email'
                    }),
            
            'subject':forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'Write subject'
                    }),

            'message':forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'Your Message'
                    }),
        }
        



