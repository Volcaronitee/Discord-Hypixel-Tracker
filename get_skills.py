import get_data


def get_skills(username: str, profile_name: str) -> {}:
    # Pick out the profile data.
    embed = {
        'title': f'Skills on [{username.upper()}: {profile_name.upper()}]',
        'url': f'http://sky.shiiyu.moe/stats/{username}/{profile_name}',
        'description': '',
        'thumbnail': f'https://mc-heads.net/head/{username}',
        'stats': {
            'experience_skill_farming': {'name': 'FARMING', 'xp': 0, 'level': 0, 'field': 'N/A'},
            'experience_skill_mining': {'name': 'MINING', 'xp': 0, 'level': 0, 'field': 'N/A'},
            'experience_skill_combat': {'name': 'COMBAT', 'xp': 0, 'level': 0, 'field': 'N/A'},
            'experience_skill_foraging': {'name': 'FORAGING', 'xp': 0, 'level': 0, 'field': 'N/A'},
            'experience_skill_fishing': {'name': 'FISHING', 'xp': 0, 'level': 0, 'field': 'N/A'},
            'experience_skill_enchanting': {'name': 'ENCHANTING', 'xp': 0, 'level': 0, 'field': 'N/A'},
            'experience_skill_alchemy': {'name': 'ALCHEMY', 'xp': 0, 'level': 0, 'field': 'N/A'},
            'experience_skill_carpentry': {'name': 'CARPENTRY', 'xp': 0, 'level': 0, 'field': 'N/A'},
            'experience_skill_taming': {'name': 'TAMING', 'xp': 0, 'level': 0, 'field': 'N/A'},
            'experience_skill_social2': {'name': 'SOCIAL', 'xp': 0, 'level': 0, 'field': 'N/A'},
            'experience_skill_runecrafting': {'name': 'RUNECRAFTING', 'xp': 0, 'level': 0, 'field': 'N/A'}
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

            for skill in embed['stats']:
                if stats.__contains__(skill):  # Makes sure API is on.
                    embed['stats'][skill]['xp'] = round(stats[skill])
                else:
                    embed['description'] = 'API is not on!'
                    return embed

            # Figure out the skill level by using Skyblock skills api.
            sb_skills = get_data.get_info('https://api.hypixel.net/resources/skyblock/skills')['skills']

            for stat in embed['stats']:
                skill_name = embed['stats'][stat]['name']
                levels = sb_skills[skill_name]['levels']
                max_level = sb_skills[skill_name]['maxLevel']

                for x in range(max_level - 1, 0, -1):
                    if embed['stats'][stat]['xp'] >= levels[x]['totalExpRequired']:
                        embed['stats'][stat]['level'] = x + 1
                        break

            # Get the field messages for each skill.
            for stat in embed['stats']:
                embed['stats'][stat]['field'] = f'LEVEL: {embed["stats"][stat]["level"]}\n'
                embed['stats'][stat]['field'] += f'XP: {embed["stats"][stat]["xp"]:,}'
            embed['description'].rstrip('\\')
        else:
            # Call last profile played on.
            for p in profiles:
                if p['selected']:
                    profile_name = p['cute_name'].lower()

            embed = get_skills(username, profile_name)
    else:
        embed['description'] = 'Hypixel account does not exist!'

    return embed
