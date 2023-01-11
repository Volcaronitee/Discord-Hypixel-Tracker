import get_data


def get_essence(username: str, profile_name: str) -> {}:
    # Pick out the profile data.
    embed = {
        'title': f'Essence on [{username.upper()}: {profile_name.upper()}]',
        'url': f'http://sky.shiiyu.moe/stats/{username}/{profile_name}',
        'description': '',
        'skin': f'https://mc-heads.net/head/{username}',
        'stats': {
            'essence_wither': {'name': 'WITHER ESSENCE', 'field': 'N/A'},
            'essence_spider': {'name': 'SPIDER ESSENCE', 'field': 'N/A'},
            'essence_undead': {'name': 'UNDEAD ESSENCE', 'field': 'N/A'},
            'essence_dragon': {'name': 'DRAGON ESSENCE', 'field': 'N/A'},
            'essence_gold': {'name': 'GOLD ESSENCE', 'field': 'N/A'},
            'essence_diamond': {'name': 'DIAMOND ESSENCE', 'field': 'N/A'},
            'essence_ice': {'name': 'ICE ESSENCE', 'field': 'N/A'},
            'essence_crimson': {'name': 'CRIMSON ESSENCE', 'field': 'N/A'},
            'essence_total': {'name': 'TOTAL ESSENCE', 'field': 'N/A'}
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
            total_essence = 0

            for stat in members:
                stats.update(members[stat])

            for stat in embed['stats']:
                embed['stats'][stat]['field'] = f'{stats.get(stat, 0):,}'
                total_essence += stats.get(stat, 0)

            embed['stats']['essence_total']['field'] = f'{total_essence:,}'
        else:
            # Call last profile played on.
            for p in profiles:
                if p['selected']:
                    profile_name = p['cute_name'].lower()

            embed = get_essence(username, profile_name)
    else:
        embed['description'] = 'Hypixel account does not exist!'

    return embed
