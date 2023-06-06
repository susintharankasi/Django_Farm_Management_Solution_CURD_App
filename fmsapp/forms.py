from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from . models import Livestock,DepStock, FarmStock, LiveFarmStock
from django.contrib.auth import get_user_model


class LoginForm (AuthenticationForm):
    username = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control p-4 mb-3', 'placeholder':'Username '}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control p-4 mb-3', 'placeholder':'Password '}))

    class Meta:
        model = get_user_model()
        fields = '__all__'
class RegisterForm (UserCreationForm):
    first_name = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class':'form-control p-4 mb-3', 'placeholder':'First Name '}))
    last_name = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class':'form-control p-4 mb-3', 'placeholder':'Last Name '}))
    username = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control p-4 mb-3', 'placeholder':'Username '}))
    password1 = forms.CharField(label='Password',max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control p-4 mb-3', 'placeholder':'Password '}))
    password2 = forms.CharField(label='Confirm Password',max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control p-4 mb-3', 'placeholder':'Confirm Password '}))

    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name','username','password1','password2']

################################################################################
################################################################################      

class DepStockForm(forms.ModelForm):
    class Meta:
        model = DepStock
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'LiveStock Name'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
            'count':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Total LiveStock Count'})
        }

class LivestockForm(forms.ModelForm):
    class Meta:
        model = Livestock
        fields = '__all__'
        widgets = {
            'department':forms.Select(attrs={'class':'form-control','placeholder':''}),
            'quantity':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Total Quantity / Litres'}),
            'sell':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sell Value'}),
            'expense':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Total Expense'}),
            'date':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Date'}),
            'time':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Time'})
        }

###############################################################################

class FarmStockForm(forms.ModelForm):
    class Meta:
        model = FarmStock
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'FarmStock Name'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
            'landarea':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Total FarmStock Area'})
        }

class LiveFarmStockForm(forms.ModelForm):
    class Meta:
        model = LiveFarmStock
        fields = '__all__'
        widgets = {
            'farmdepartment':forms.Select(attrs={'class':'form-control','placeholder':''}),
            'quantity':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Total Quantity'}),
            'sell':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sell Value'}),
            'expense':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Total Expense'}),
            'harvestdate':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Harvest Date'}),
            'crop':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Crop Type'}),
            'sellingdate':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Selling Date'}),
            'time':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Time'})
        }

##################################################################################