from django.forms import ModelForm
from app.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'phone' , 'email']
