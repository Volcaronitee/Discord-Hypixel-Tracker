import requests

API_KEY = "03efb117-141e-4d6e-8aab-8161ee6816f0"


def get_info(call):
    r = requests.get(call)
    return r.json()


def load_profiles(username: str) -> {}:
    url = f'https://api.mojang.com/users/profiles/minecraft/{username}?'
    check = requests.get(url)
    status = check.status_code

    if status != 204:  # Check if minecraft account exists.
        r = get_info(url)
        uuid = r['id']

        data = get_info(f"https://api.hypixel.net/skyblock/profiles?key={API_KEY}&uuid={uuid}")
        profiles = data['profiles']
    else:
        profiles = {}

    return profiles


def get_profile(profiles: {}, profile_name: str) -> {}:
    profile = {}

    # Find desired profile.
    for p in profiles:
        if p['cute_name'].lower() == profile_name:
            profile = p

    return profile