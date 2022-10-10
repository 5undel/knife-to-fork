from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Topic



class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class TopicRoom(ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'


