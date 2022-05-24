import os
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from dotenv import load_dotenv
from pandas import read_excel
import pandas as pd
from colr import color

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)
client = discord.Client()

excelSheet = 'Sheet1'
filePath = os.getenv('READER_FILE_PATH')
reader = read_excel(filePath, sheet_name=excelSheet)

serverName = os.getenv('SERVER_NAME')


@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=serverName)
    print(color(f'{bot.user} has connected to the {guild.name} Discord Server!', fore='green'))


@bot.command(name='assignRoles', hidden=True, pass_context=True)
@has_permissions(manage_roles=True)
async def assign_roles(ctx):
    guild = discord.utils.get(bot.guilds, name=serverName)

    if "moderator" in [i.name.lower() for i in ctx.author.roles]:
        index = 0
        for username in reader['Username']:
            role_name = reader['Role'][index]
            role_id = discord.utils.find(lambda r: r.name == role_name, guild.roles)
            member = discord.utils.find(lambda m: m.name == username, guild.members)

            if role_id is not None:
                if member is not None:
                    await member.add_roles(role_id)
                    print(f'{role_name} role added to {member}')
                else:
                    print(color(f'Member not found. Please check row {index} in the given file', fore='red'))
            else:
                print(color(f'Role not found. Please check row {index} in the given file', fore='red'))

            index += 1
    else:
        await ctx.channel.send("You do not have the proper role to use this command")


@bot.command(name='exportRoles', hidden=True, pass_context=True)
@has_permissions(manage_roles=True)
async def export_roles(ctx):
    if "moderator" in [i.name.lower() for i in ctx.author.roles]:

        names = []
        ids = []
        roles = []

        try:
            for member in ctx.channel.members:
                if member.bot is True:
                    continue

                my_roles = []

                for role in member.roles:
                    if role.name != '@everyone':
                        my_roles.append(role.name)

                my_roles = list(dict.fromkeys(my_roles))
                names.append(member.name)
                ids.append(member.discriminator)
                roles.append(my_roles)

            info = pd.DataFrame({
                'Username': names,
                'ID': ids,
                'Roles': roles
            })

            writer = pd.ExcelWriter('exportedRoles.xlsx', engine='xlsxwriter')
            info.to_excel(writer, index=False)

            writer.save()
            print(color('Data exported successfully', fore='green'))
        except Exception:
            print(color('There has been an issue with exporting the file. Please contact Heykan#9170 on Discord', fore='red'))


bot.run(TOKEN)
