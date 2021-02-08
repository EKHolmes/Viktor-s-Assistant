import os
import discord
from keep_alive import keep_alive
from discord.ext import commands
import slimepedia

bot = commands.Bot(
	command_prefix="//",
	case_insensitive=True  
)

bot.author_id = 725198437393367112

@bot.event 
async def on_ready():
    print("Ready")
    print(bot.user)

@bot.command(name="hellothere")
async def hellothere(ctx):
  await ctx.send("General Kenobi.")

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

@bot.command(name="fieldtest")
async def fieldtest(ctx):
  resultEmbed = discord.Embed()
  resultEmbed.add_field(name="Test Name", value="Test Value", inline=(True))
  await ctx.send(embed=resultEmbed)

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET") 
bot.run(token)