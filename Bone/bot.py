import discord
import random
import asyncio
import os
import sys
import platform
from discord.ext.commands import Bot
from discord.ext import commands

project_root = os.path.dirname(os.path.dirname(__file__))
if not os.path.isfile(f"{project_root}/Bone/config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

intents = discord.Intents.default()
intents.members = True
intents.messages = True
bot = Bot(command_prefix=config.BOT_PREFIX, intents=intents)

# The code in this even is executed when the bot is ready
@bot.event
async def on_ready():
    bot.loop.create_task(status_task())
    print(f"Logged in as {bot.user.name}")
    print(f"Discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")


# Setup the game status task of the bot
async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game("Strikes!"))
        await asyncio.sleep(60)
        await bot.change_presence(activity=discord.Game("Raids!"))
        await asyncio.sleep(60)
        await bot.change_presence(activity=discord.Game(f"{config.BOT_PREFIX} prefix"))
        await asyncio.sleep(60)
        await bot.change_presence(activity=discord.Game("Schmelztiegel!"))
        await asyncio.sleep(60)
        await bot.change_presence(activity=discord.Game("Prüfungen des Osiris!"))
        await asyncio.sleep(60)
        await bot.change_presence(activity=discord.Game("Eisenbanner!"))
        await asyncio.sleep(60)
        await bot.change_presence(activity=discord.Game("Dungeons!"))
        await asyncio.sleep(60)

# Removes the default help command of discord.py to be able to create our custom help command.
bot.remove_command("help")

if __name__ == "__main__":
    for extension in config.STARTUP_COGS:
        try:
            bot.load_extension(extension)
            extension = extension.replace("cogs.", "")
            print(f"Loaded extension '{extension}'")
        except Exception as e:
            exception = f"{type(e).__name__}: {e}"
            extension = extension.replace("cogs.", "")
            print(f"Failed to load extension {extension}\n{exception}")

# The code in this event is executed every time someone sends a message, with or without the prefix
@bot.event
async def on_message(message):
    # Ignores if a command is being executed by a bot or by the bot itself
    if message.author == bot.user or message.author.bot:
        return
    else:
        if message.author.id not in config.BLACKLIST:
            # Process the command if the user is not blacklisted
            await bot.process_commands(message)
        else:
            # Send a message to let the user know he's blacklisted
            context = await bot.get_context(message)
            embed = discord.Embed(
                title="You're blacklisted!",
                description="Ask the owner to remove you from the list if you think it's not normal.",
                color=0x00FF00
            )
            await context.send(embed=embed)

@bot.event
async def on_raw_reaction_add(payload):               
    channel_id = payload.channel_id    
    if channel_id in config.RAID_CHANNELS:
        guild_id = payload.guild_id
        member_id = payload.user_id        
        if payload.user_id != config.APPLICATION_ID:
            guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)            
            if guild is not None:
                channel = bot.get_channel(payload.channel_id)
                msg = await channel.fetch_message(payload.message_id)            
                embed = msg.embeds[0]                
                member = discord.utils.find(lambda m : m.id == member_id, guild.members)                
                if member is not None:                                        
                    if embed.title.startswith("Raid:"):                        
                        if payload.emoji.name == '1️⃣':                                                          
                            embed.set_field_at(
                                0,                                    
                                name="1️⃣",
                                value=f"{member.display_name}",
                                inline=True
                            )                    
                            await msg.edit(embed=embed)
                        elif payload.emoji.name == '2️⃣':                                                          
                            embed.set_field_at(
                                1,                                    
                                name="2️⃣",
                                value=f"{member.display_name}",
                                inline=True
                            )                    
                            await msg.edit(embed=embed)
                        elif payload.emoji.name == '3️⃣':                                                          
                            embed.set_field_at(
                                2,                                    
                                name="3️⃣",
                                value=f"{member.display_name}",
                                inline=True
                            )                    
                            await msg.edit(embed=embed)
                        elif payload.emoji.name == '4️⃣':                                                          
                            embed.set_field_at(
                                3,                                    
                                name="4️⃣",
                                value=f"{member.display_name}",
                                inline=True
                            )                    
                            await msg.edit(embed=embed)
                        elif payload.emoji.name == '5️⃣':                                                          
                            embed.set_field_at(
                                4,                                    
                                name="5️⃣",
                                value=f"{member.display_name}",
                                inline=True
                            )                    
                            await msg.edit(embed=embed)
                        elif payload.emoji.name == '6️⃣':                                                          
                            embed.set_field_at(
                                5,                                    
                                name="6️⃣",
                                value=f"{member.display_name}",
                                inline=True
                            )                    
                            await msg.edit(embed=embed)

#Get reaction remove Events
@bot.event
async def on_raw_reaction_remove(payload):            
    channel_id = payload.channel_id
    if channel_id in config.RAID_CHANNELS:
        guild_id = payload.guild_id
        member_id = payload.user_id        
        if payload.user_id != config.APPLICATION_ID:
            guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)
            if guild is not None:
                channel = bot.get_channel(payload.channel_id)
                msg = await channel.fetch_message(payload.message_id)            
                embed = msg.embeds[0]                
                member = discord.utils.find(lambda m : m.id == member_id, guild.members)                
                if member is not None:                   
                    if embed.title.startswith("Raid:"): 
                        reaction = discord.utils.get(msg.reactions, emoji=payload.emoji.name)                        
                        print(reaction.count)        
                        if reaction and reaction.count == 1:                                                     
                            if payload.emoji.name == '1️⃣':                            
                                embed.set_field_at(
                                    0,                                    
                                    name="1️⃣",
                                    value="frei",
                                    inline=True
                                )                    
                                await msg.edit(embed=embed)
                            elif payload.emoji.name == '2️⃣':                                                          
                                embed.set_field_at(
                                    1,                                    
                                    name="2️⃣",
                                    value="frei",
                                    inline=True
                                )                    
                                await msg.edit(embed=embed)
                            elif payload.emoji.name == '3️⃣':                                                          
                                embed.set_field_at(
                                    2,                                    
                                    name="3️⃣",
                                    value="frei",
                                    inline=True
                                )                    
                                await msg.edit(embed=embed)
                            elif payload.emoji.name == '4️⃣':                                                          
                                embed.set_field_at(
                                    3,                                    
                                    name="4️⃣",
                                    value="frei",
                                    inline=True
                                )                    
                                await msg.edit(embed=embed)
                            elif payload.emoji.name == '5️⃣':                                                          
                                embed.set_field_at(
                                    4,                                    
                                    name="5️⃣",
                                    value="frei",
                                    inline=True
                                )                    
                                await msg.edit(embed=embed)
                            elif payload.emoji.name == '6️⃣':                                                          
                                embed.set_field_at(
                                    5,                                    
                                    name="6️⃣",
                                    value="frei",
                                    inline=True
                                )                    
                                await msg.edit(embed=embed)

# The code in this event is executed every time a command has been *successfully* executed
@bot.event
async def on_command_completion(ctx):
    fullCommandName = ctx.command.qualified_name
    split = fullCommandName.split(" ")
    executedCommand = str(split[0])
    print(
        f"Executed {executedCommand} command in {ctx.guild.name} by {ctx.message.author} (ID: {ctx.message.author.id})")

# The code in this event is executed every time a valid commands catches an error
@bot.event
async def on_command_error(context, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(
            title="Error!",
            description="This command is on a %.2fs cooldown" % error.retry_after,
            color=0x00FF00
        )
        await context.send(embed=embed)
    raise error

# Run the bot with the token
bot.run(config.TOKEN)