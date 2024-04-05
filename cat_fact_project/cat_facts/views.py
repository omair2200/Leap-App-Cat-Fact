from django.http import JsonResponse
import aiohttp
import asyncio
from django.views.decorators.csrf import csrf_exempt

last_fact = None

@csrf_exempt
def health_check(request):
    return JsonResponse({'status': 'ok'}, status=200)

async def fetch_data():
    try:
        url = "https://cat-fact.herokuapp.com/facts"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                return data
    except Exception as e:
        raise e

@csrf_exempt
async def fetch_fact(request):
    global last_fact
    try:
        asyncio.create_task(fetch_data())  # fetch_fact endpoint wont wait for the endpoint now
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)

@csrf_exempt
def get_fact(request):
    global last_fact
    try:
        if last_fact:
            return JsonResponse({'fact': last_fact})
        else:
            return JsonResponse({'error': 'no_task_has_been_queued_yet'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
