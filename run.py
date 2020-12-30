#!/usr/bin/env python3
import discord, json, lib
from bot import WriterBot
from discord.ext import commands

# Load the settings for initial setup
config = lib.get('./settings.json')

# Load the Bot object
status = discord.Game( 'Booting up...' )
bot = WriterBot(command_prefix=WriterBot.load_prefix, activity=status)

# Load all commands
bot.load_commands()

# Start the bot
bot.run(config.token)
