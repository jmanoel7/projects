from django.shortcuts import render
import requests
from django.conf import settings
from django.core.cache import cache
import logging

logger = logging.getLogger(__name__)

def fetch_products(quantity=10):
    """
    Fetch products from Faker API
    """
    cache_key = f'faker_products_{quantity}'
    cached_products = cache.get(cache_key)
    
    if cached_products:
        return cached_products
        
    try:
        response = requests.get(
            f'https://fakerapi.it/api/v2/products',
            params={'_quantity': quantity},
            timeout=5
        )
        response.raise_for_status()
        data = response.json()
        
        # Cache the results for 1 hour
        cache.set(cache_key, data['data'], 3600)
        
        return data['data']
    except requests.RequestException as e:
        logger.error(f"Error fetching products from Faker API: {str(e)}")
        return []

def product_list(request):
    """
    View to display products fetched from Faker API
    """
    # Get quantity from query params, default to 10
    quantity = int(request.GET.get('quantity', 10))
    
    # Limit maximum quantity to prevent abuse
    quantity = min(quantity, 100)
    
    products = fetch_products(quantity)
    
    context = {
        'products': products,
        'current_quantity': quantity
    }
    
    return render(request, 'products/index.html', context)