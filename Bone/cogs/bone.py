import os
import sys
import discord
import platform
import random
from discord.ext import commands

project_root = os.path.dirname(os.path.dirname(__file__))
if not os.path.isfile(f"{project_root}/config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

class Bone(commands.Cog, name="bone"):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="raid")
    async def raid(self, context, *args):
        """
        Erstelle einen neuen Raideintrag und reagiert auf die Nummern zum Teilnehmen.
        """        
        raid_entry = " ".join(args)        
        embed = discord.Embed(            
            title=f"Raid: {raid_entry}",
            description=f"Teilnehmer:\n",
            color=0x0068FF
        )        
        embed.add_field(
            name="1️⃣",
            value="frei",
            inline=True
        )
        embed.add_field(
            name="2️⃣",
            value="frei",
            inline=True
        )
        embed.add_field(
            name="3️⃣",
            value="frei",
            inline=True
        )
        embed.add_field(
            name="4️⃣",
            value="frei",
            inline=True
        )
        embed.add_field(
            name="5️⃣",
            value="frei",
            inline=True
        )
        embed.add_field(
            name="6️⃣",
            value="frei",
            inline=True
        )
        embed.set_footer(
            text=f"Ein neuer Raid wurde von {context.message.author} erstellt, • React zum Beitritt!"
        )        
        embed_message = await context.send(embed=embed)
        await embed_message.add_reaction("1️⃣")        
        await embed_message.add_reaction("2️⃣")        
        await embed_message.add_reaction("3️⃣")        
        await embed_message.add_reaction("4️⃣")        
        await embed_message.add_reaction("5️⃣")        
        await embed_message.add_reaction("6️⃣")      
        await context.message.delete()
        for x in config.NOTIFY_CHANNELS:             
            if x != context.channel.id:
                channel = self.bot.get_channel(x)      
                if channel:      
                    await channel.send(f'Moin,\nauf dem Discord {context.guild} wurde ein Raid mit dem Titel "{raid_entry}" erstellt.\nSchaut doch mal rein, ob das was für euch ist.')
                else:
                    print(f'ChannelID:{x} konnte nicht gefunden werden.')
    
def setup(bot):
    bot.add_cog(Bone(bot))