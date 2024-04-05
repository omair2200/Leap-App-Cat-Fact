import dramatiq
import requests
from .models import CatFact

@dramatiq.actor
def fetch_cat_fact():
    response = requests.get('https://cat-fact.herokuapp.com/facts')
    facts = response.json()
    facts_text = facts[0]['text']
    print(facts_text)
    if facts_text:
        CatFact.objects.create(fact=facts_text)
        return facts_text
    return None
