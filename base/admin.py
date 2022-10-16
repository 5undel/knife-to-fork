from django.contrib import admin
from .models import Room, Topic, Message, ProfileBio


admin.site.register(ProfileBio)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
