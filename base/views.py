from django.shortcuts import render

# Create your views here.

rooms = [
    {
        'id': 1,
        'name' : 'Conference Room A',
    },
    {
        'id': 2,
        'name' : 'Home Group Room',
    },
    {
        'id': 3,
        'name' : 'Workshop Room',
    },
    {
        'id': 4,
        'name' : 'Meeting Room',
    },
    {
        'id': 5,
        'name' : 'Seminar Room',
    },
    {
        'id': 6,
        'name' : 'Board Room',
    },
    {
        'id': 7,
        'name' : 'Training Room',
    },
    {
        'id': 8,
        'name' : 'Classroom',
    },
    {
        'id': 9,
        'name' : 'Lecture Room',
    },
    {
        'id': 10,
        'name' : 'Auditorium',
    },
    {
        'id': 11,
        'name' : 'Exhibition Hall',
    },
    {
        'id': 12,
        'name' : 'Ballroom',
    },
    {
        'id': 13,
        'name' : 'Banquet Hall',
    },
    {
        'id': 14,
        'name' : 'Function Room',
    },
    {
        'id': 15,
        'name' : 'Party Room',
    },
    {
        'id': 16,
        'name' : 'Event Space',
    },
    {
        'id': 17,
        'name' : 'Studio',
    },
    {
        'id': 18,
        'name' : 'Office Space',
    },
    {
        'id': 19,
        'name' : 'Co-working Space',
    },
    {
        'id': 20,
        'name' : 'Hot Desk',
    }
]

def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request, pk):
    context = {'roomName': rooms[int(pk) - 1], 'rooms': rooms, 'pk': pk}
    return render(request, 'base/room.html', context)