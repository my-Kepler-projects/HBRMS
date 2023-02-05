from django.contrib import admin
from .models import *

admin.site.register(Patient)
admin.site.register(RoomOccupancy)
admin.site.register(RoomReservaion)
admin.site.register(RoomType)
admin.site.register(HospitalRoom)
admin.site.register(Doctor)
