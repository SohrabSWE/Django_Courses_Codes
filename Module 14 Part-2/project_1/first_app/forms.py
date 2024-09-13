from django import forms
from first_app.models import StudentModel
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels = {
            'name' : 'Studnet Name',
            'roll' : 'Studnet Roll',
        }
        help_texts = {
            'name' : 'Write your full name'
        }
        error_messages = {
            'name' : {'required' : 'Your name is required'}
        }