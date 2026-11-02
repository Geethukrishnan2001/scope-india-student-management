from django import forms
from .models import *

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'