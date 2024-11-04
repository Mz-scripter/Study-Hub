from django.forms import ModelForm
from .models import Room

# This will create the form based on the what is in the Room Model
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'