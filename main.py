## Importing Libraries ##

import os
import discord
from keep_alive import keep_alive
from discord.ext import commands
import slimepedia


## Setting Up the Bot Class ##

# Sets the bot prefix for Discord commands.
bot = commands.Bot(
	command_prefix="//",
	case_insensitive=True  
)

# Defines the Discord ID of me, the author.
bot.author_id = 808213890843672606

# Outputs a Ready statement to the console to let me know the bot is running.
@bot.event 
async def on_ready():
    print("Ready")
    print(bot.user)



## Defining Bot Commands ##

# A test command to make sure the bot is working.
@bot.command(name="hellothere")
async def hellothere(ctx):
  await ctx.send("General Kenobi.")

# Returns an embed with information about the slime specified by the user. Takes info from slimepedia.py
@bot.command(name="slime")
async def slime(ctx, slimeID):
  slimedict = slimepedia.slimes[slimeID]
  embedDesc = f"**Diet:** {slimedict['diet']}\n"
  embedDesc += f"**Favorite Food:** {slimedict['fav']}\n"
  embedDesc += f"**Habitats:** {slimedict['habitats']}\n"
  embedDesc += f"**Base Plort Price:** {slimedict['plort_base_price']} newbucks.\n"
  embedDesc += f"**Demeanor:** {slimedict['demeanor']}\n"
  embedDesc += f"**Slime Toy:** {slimedict['toy']}\n"
  embedDesc += f"**Slimeology:** {slimedict['slimeology']}\n"
  embedDesc += f"**Risks:** {slimedict['risks']}\n"
  embedDesc += "**Icon:**"
  resultEmbed = discord.Embed(title=f"***{slimedict['name']}***",description=embedDesc)
  resultEmbed.set_image(url=slimedict['icon_url'])
  await ctx.send(embed=resultEmbed)


## Activating The Bot ##

# Creates a webpage that is constantly pinged by an external source to keep the repl running.
keep_alive()

# Defines the token of the bot. Taken from a .env file.
token = os.environ.get("DISCORD_BOT_SECRET") 

# Activates the bot via the Discord api.
bot.run(token)