from django import forms
def validation_is_a(svalue):
    if svalue[0]=='a':
        raise forms.ValidationError('first letter not start a')
def validation_is_length(sname):
    if len(sname)<=3:
        raise forms.ValidationError('length is more than 3')
def validation_is_email(smail):
    if smail[0]==smail.isdigit():
        raise forms.ValidationError('first letter not start number')
class Studentform(forms.Form):
    sname=forms.CharField(max_length=80,validators=[validation_is_a,validation_is_length])
    sage=forms.IntegerField()
    saddress=forms.CharField(max_length=50)
    semail=forms.EmailField(validators=[validation_is_email])