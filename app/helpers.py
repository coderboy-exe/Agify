from datetime import datetime
import json

import requests

from app.constants import AGIFY_URL


def get_birthyear(age: int)->int:
    """Computes birth year, given age
    
    Args:
        age (int): age
        
    Returns:
        int: birth year
    """
    birth_year = (datetime.now().year) - age
    return birth_year

def compute_details(name: str)->dict:
    """computes and returns name, age and birthyear for given name

    Args:
        name (str): the input name

    Returns:
        dict: dictionary containing the name, age and birthyear
    """
    response = requests.get(url=f"{AGIFY_URL}?name={name}")
    data = json.loads(response.text)
    age = data.get("age")
    birth_year = get_birthyear(age)
    
    return {
        "name": name,
        "age": age,
        "date_of_birth": birth_year
    }
    