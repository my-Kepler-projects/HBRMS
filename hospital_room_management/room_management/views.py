# from django.core.exceptions import ValidationError

## Exception Handler While Reserving room
# def create_reservation(request):
#     if request.method == 'POST':
#         form = RoomReservationForm(request.POST)

#         if form.is_valid():
#             try:
#                 reservation = form.save()
#                 return redirect('reservation_list')
#             except ValidationError as e:
#                 form.add_error('room_number', e)
#     else:
#         form = RoomReservationForm()

#     context = {
#         'form': form
#     }

#     return render(request, 'room_reservation/create.html', context)