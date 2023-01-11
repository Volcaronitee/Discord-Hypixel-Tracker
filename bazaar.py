import get_data
from pprint import pprint


def get_products():
    return get_data.get_info('https://api.hypixel.net/skyblock/bazaar')['products']


def bz(item: str) -> {}:
    # Pick out the profile data.
    embed = {
        'title': f'{item.replace("_", " ")}',
        'url': f'https://bazaartracker.com/product/{item}',
        'description': '',
        'thumbnail': f'https://sky.lea.moe/item/{item}',
        'stats': {
            'buyPrice': {'name': 'INSTA BUY', 'field': 'N/A'},
            'buyVolume': {'name': 'BUY VOLUME', 'field': 'N/A'},
            'buyMovingWeek': {'name': 'WEEKLY BUY', 'field': 'N/A'},
            'sellPrice': {'name': 'INSTA SELL', 'field': 'N/A'},
            'sellVolume': {'name': 'SELL VOLUME', 'field': 'N/A'},
            'sellMovingWeek': {'name': 'WEEKLY SELL', 'field': 'N/A'},
        }
    }

    product = get_products().get(item, 0)

    if product != 0:
        product_stats = product.get('quick_status')

        for stat in embed['stats']:
            embed['stats'][stat]['field'] = round(product_stats[stat])
    else:
        embed['description'] = "Item not found!"

    return embed
