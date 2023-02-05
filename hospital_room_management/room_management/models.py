from django.db import models
from django.core.validators import ValidationError


class RoomType(models.Model):
    room_type = models.CharField(max_length=255)

    def __str__(self):
        return self.room_type

class HospitalRoom(models.Model):
    room_number = models.CharField(max_length=255, blank=False, null=False, primary_key=True)
    room_capacity = models.IntegerField()
    room_amenities = models.CharField(max_length=255)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)

    def __str__(self):
        return f'Room {self.room_number} - Room Type: {self.room_type}'

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
class Patient(models.Model):
    GENDER_OPTIONS = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    
    STATUS_CHOICE = (
        ('Upcoming', 'Upcoming'),
        ('In-Progress', 'In-Progress'),
        ('Completed', 'Completed')
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    telephone = models.CharField(max_length=13)
    date_admitted = models.DateTimeField(auto_now_add=True)
    room_number = models.ForeignKey(HospitalRoom, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=STATUS_CHOICE)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
     
class RoomReservaion(models.Model):
    room = models.ForeignKey(HospitalRoom, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    RRN = models.CharField(max_length=13)

    def save(self, *args, **kwargs):
        if self.is_room_occupied(self.room):
            raise ValidationError('This room is already occupied')
        super(RoomReservaion, self).save(*args, **kwargs)
    
    @staticmethod
    def is_room_occupied(room):
        return RoomReservaion.objects.filter(room_number=room, end_date__isnull=True).exists()

class RoomOccupancy(models.Model):
    STATUS_CHOICE = (
        ('Occupied', 'Occupied'),
        ('Free', 'Free'),
        ('Out of Service', 'Out of Service')
    )
    room = models.ForeignKey(HospitalRoom, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    checkin_date = models.DateTimeField()
    checkout_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICE)

    def __str__(self) -> str:
        return f'{self.room} - Room Type: {self.room.room_type} - {self.checkin_date} - {self.status}'