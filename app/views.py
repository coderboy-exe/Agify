import json
import requests
from datetime import datetime

from django.core.cache import cache

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from app.helpers import compute_details


# Create your views here.
@api_view(['GET'])
def index(request):
    return Response("Service running", status.HTTP_200_OK)

@api_view(['POST'])
def get_age(request):
    if not request.data:
        return Response("Please provide a valid name. \n Usage: {'name': 'example_name'}", status.HTTP_400_BAD_REQUEST)
    
    name = request.data.get("name")
    if not name or not isinstance(name, str):
        return Response("Name should be a string. \n Usage: {'name': 'example_name'}", status.HTTP_400_BAD_REQUEST)
    
    name = name.lower()
    
    cache_key = f"get_age_{name}"
    cached_data = cache.get(cache_key)
    
    if cached_data is None:
        result = compute_details(name)
        cache.set(cache_key, result, timeout=3600)
        return Response(result, status.HTTP_200_OK)

    return Response(cached_data, status.HTTP_200_OK)

