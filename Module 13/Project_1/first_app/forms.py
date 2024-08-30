from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label="User Name", help_text="Total length is within 70 characters", widget=forms.Textarea)
    email = forms.EmailField(label="User Email")
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs = {'type' : 'date'}))
    appoinment = forms.DateTimeField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices = CHOICES, widget=forms.RadioSelect)
    MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)
    file = forms.FileField()

# class StudentData(forms.Form):
#     name =forms.CharField(widget=forms.TextInput)
#     email =forms.CharField(widget=forms.EmailInput)

    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10 :
    #         raise forms.ValidationError("Enter a name with at least 10 chracter")
    #     else:
    #         return valname
    
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Enter email must contain .com")
    #     else:
    #         return valemail
        
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']

    #     if len(valname) < 10 :
    #         raise forms.ValidationError("Enter a name at least 10 character")
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Enter email must contain .com")

def len_check(value):
    if len(value) < 10 :
        raise forms.ValidationError("Enter at least 10 character")

class StudentData(forms.Form):
    name =forms.CharField(widget=forms.TextInput, validators=[validators.MaxLengthValidator(10, message="Enter a name at least 10 character")])
    text = forms.CharField(widget=forms.TextInput, validators=[len_check])
    email =forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message="Enter a valid email")])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34,message="Enter age max 34"), validators.MinValueValidator(24,message="Enter age  at least 24")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','jpg'],message="File must be ended .pdf")])


class PasswordProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        if val_pass != val_conpass:
            raise forms.ValidationError("Password not matching")
