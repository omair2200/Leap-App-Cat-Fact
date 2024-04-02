from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt

# Global variable to store the last fetched fact
last_fact = None

@csrf_exempt
def health_check(request):
    return JsonResponse({'status': 'ok'}, status=200)


@csrf_exempt
def fetch_fact(request):
    global last_fact
    try:
        url = "https://cat-fact.herokuapp.com/facts"
        response = requests.get(url)
        data = response.json()
        if data:
            last_fact = data[0]['text']
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'No facts found'}, status=404)
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
