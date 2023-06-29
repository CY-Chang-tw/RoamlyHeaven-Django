from django import forms


class InForm(forms.Form):
    indate = forms.DateField()

class OutForm(forms.Form):
    outdate = forms.DateField()

class P_Num(forms.Form):
    p_num = forms.IntegerField()

class City(forms.Form):
    city = forms.CharField()