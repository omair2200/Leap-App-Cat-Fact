from django.http import JsonResponse
from .models import CatFact
from .tasks import fetch_cat_fact



def health_check(request):
    return JsonResponse({'status': 'ok'})

def fetch_fact(request):
    fetch_cat_fact.send()
    return JsonResponse({'success': True})



def get_fact(request):
    try:
        last_fact = CatFact.objects.latest('fetched_at')
        CatFact.objects.all().delete() #Added this for multiple trial and error testing
        return JsonResponse({'fact': last_fact.fact})
    except CatFact.DoesNotExist:
        return JsonResponse({'error': 'no_task_has_been_queued_yet'})
