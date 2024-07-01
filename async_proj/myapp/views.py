import aiohttp
from django.http import JsonResponse
from asgiref.sync import sync_to_async
import asyncio
from .models import Animals
import certifi,ssl
sslcontext = ssl.create_default_context(cafile=certifi.where())


@sync_to_async
def get_db_obj():
    return list(Animals.objects.values())

async def async_view(request):
    animals = await get_db_obj()
    return JsonResponse({'animals': animals})

async def get_first_animal(request):
    animals = await get_db_obj()[0]
    return JsonResponse({'animals': animals})


async def get_weather_data():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'lat': '49.988358',
        'lon': '36.232845',
        'appid': 'e5b99dfce20dd3ca7d830f1236baa62a'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, ssl=sslcontext) as response:
            if response.status == 200:
                return await response.json()
            else:
                return {'error': 'Could not fetch weather data'}
            
async def weather_view(request):
    weather_data = await get_weather_data()
    return JsonResponse(weather_data)

