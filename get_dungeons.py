import get_data
from pprint import pprint


def get_dungeons(username: str, profile_name: str) -> {}:
    # Pick out the profile data.
    embed = {
        'title': f'Dungeons on [{username.upper()}: {profile_name.upper()}]',
        'url': f'http://sky.shiiyu.moe/stats/{username}/{profile_name}',
        'description': 'IN PROGRESS',
        'skin': f'https://mc-heads.net/head/{username}',
        'stats': {
        }
    }

    # Get skyblock profiles
    profiles = get_data.load_profiles(username)

    if profiles is not None and len(profiles) > 0:  # Checks if Hypixel account exists.
        profile = get_data.get_profile(profiles, profile_name)

        if len(profile) > 0:  # Checks if profile exists.
            # Retrieve the stats of the profile in one dictionary.
            members = profile['members']
            stats = {}

            for stat in members:
                stats.update(members[stat])

            for stat in stats:
                print(stat)
        else:
            # Call last profile played on.
            for p in profiles:
                if p['selected']:
                    profile_name = p['cute_name'].lower()

            embed = get_dungeons(username, profile_name)
    else:
        embed['description'] = 'Hypixel account does not exist!'

    return embed
