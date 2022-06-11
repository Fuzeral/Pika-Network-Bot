import discord
from discord.ext import commands
from bot_config import token
import sys
import os
import json
import traceback



prefix = "."



client = commands.Bot(command_prefix=f"{prefix}")

with open ('./config/modules.json', 'r') as f:
    cogsData = json.load(f)
    module = cogsData['extensions']

if __name__ == "__main__":
    for values in module:
        try:
            client.load_extension(values)
            print(f"[/] loaded | {values}")
        except:
            print(f'Error loading {values}', file=sys.stderr)
            traceback.print_exc()


client.run(token)