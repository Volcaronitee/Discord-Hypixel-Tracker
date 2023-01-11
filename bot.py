import asyncio

import discord
from discord import app_commands
from discord.ext import commands
import typing

import get_skills
import get_slayer
import get_dungeons
import get_essence

import bazaar
import get_auction


def get_embed(data: {}) -> discord.Embed:
    embed = discord.Embed(title=data.get('title'),
                          url=data.get('url'),
                          description=data.get('description'),
                          color=discord.Colour.red())
    embed.set_thumbnail(url=data.get('thumbnail'))
    embed.set_footer(text='by Volcaronitee#0233', icon_url='https://mc-heads.net/head/volcaronitee')

    for stat in data['stats']:
        embed.add_field(name=f'**{data["stats"][stat]["name"]}:**',
                        value=data["stats"][stat]['field'],
                        inline=True)

    return embed


def run():
    token = 'MTA1NzAwMjE0MjY1ODk5NDI0Ng.GhUAfA.NRUKssEtiYL5pgv8TiNAnu3I6kpH3Ava2CmjHs'
    client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        try:
            synced = await client.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(e)

    # SKILLS
    @client.tree.command(name="skills", description="View your Skyblock skills!")
    @app_commands.describe(ign="Enter your Minecraft ign!", profile="Enter your Hypixel profile!")
    async def skills(interaction: discord.Interaction, ign: str, profile: str):
        await interaction.response.defer()

        # Get embed info.
        data = get_skills.get_skills(ign, profile)

        # Create the embed.
        embed = get_embed(data)

        await interaction.followup.send(embed=embed)

    # SLAYERS
    @client.tree.command(name="slayers", description="View your Skyblock slayer stats!")
    @app_commands.describe(ign="Enter your Minecraft ign!", profile="Enter your Hypixel profile!")
    async def slayers(interaction: discord.Interaction, ign: str, profile: str):
        await interaction.response.defer()

        # Get embed info.
        data = get_slayer.get_slayer(ign, profile)

        # Create the embed.
        embed = get_embed(data)

        await interaction.followup.send(embed=embed)

    # DUNGEONS
    @client.tree.command(name="dungeons", description="View your Skyblock dungeon stats!")
    @app_commands.describe(ign="Enter your Minecraft ign!", profile="Enter your Hypixel profile!")
    async def dungeons(interaction: discord.Interaction, ign: str, profile: str):
        await interaction.response.defer()

        # Get embed info.
        data = get_dungeons.get_dungeons(ign, profile)

        # Create the embed.
        embed = get_embed(data)

        await interaction.followup.send(embed=embed)

    # ESSENCE
    @client.tree.command(name="essence", description="View your essence!")
    @app_commands.describe(ign="Enter your Minecraft ign!", profile="Enter your Hypixel profile!")
    async def dungeons(interaction: discord.Interaction, ign: str, profile: str):
        await interaction.response.defer()

        # Get embed info.
        data = get_essence.get_essence(ign, profile)

        # Create the embed.
        embed = get_embed(data)

        await interaction.followup.send(embed=embed)

    # AUCTION
    @client.tree.command(name="ah", description="View your Skyblock auctions!")
    @app_commands.describe(ign="Enter your Minecraft ign!", profile="Enter your Hypixel profile!")
    async def skills(interaction: discord.Interaction, ign: str, profile: str):
        await interaction.response.defer()

        # Get embed info.
        data = get_auction.ah(ign, profile)

        # Create the embed.
        embed = get_embed(data)

        await interaction.followup.send(embed=embed)

    # BAZAAR
    async def bz_autocomplete(interaction: discord.Interaction, current: str) -> typing.List[app_commands.Choice[str]]:
        data = []
        products = list(bazaar.get_products().keys())
        item = current.lower().replace(" ", "_")

        for product in products:
            if item in product.lower():
                data.append(app_commands.Choice(name=product, value=product))

        return data[0:25]

    @client.tree.command(description="View bazaar item stats!")
    @app_commands.describe(item="Enter the product name!")
    @app_commands.autocomplete(item=bz_autocomplete)
    async def bz(interaction: discord.Interaction, item: str):
        await interaction.response.defer()

        # Get embed info.
        item = item.upper().replace(" ", "_")
        data = bazaar.bz(item)

        # Create the embed.
        embed = get_embed(data)

        await interaction.followup.send(embed=embed)

    client.run(token, root_logger=True)
