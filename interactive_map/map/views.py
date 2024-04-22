from django.http import JsonResponse
from django.shortcuts import render
from .models import User

def index(request):
    return render(request, 'index.html')

def save_location(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        User.objects.create(name=name, latitude=latitude, longitude=longitude)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_shortest_route(request):
    shortest_route_data = {
        'route': '...',
        'distance': '...',
        'duration': '...',
    }
    return JsonResponse(shortest_route_data)