import discord
from discord.ext import commands 

client = discord.Client()

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hi"):

        if str(message.author) == "CodePoltergeist#8379": 
            await message.channel.send("Hello " + str(message.author) + "!")
        else:
            await message.channel.send("Heya dude, Wassup?")
    
    if str(message.channel) == "pictures" and message.content != "":
        
        await message.channel.purge(limit=1)

client.run('NzQ3Njk3ODU1MTk5OTY5Mjgx.X0Sp5A.Q--ejtIyfw579qI6IJ4NDUsJX70')

