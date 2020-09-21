import discord
import random
from discord.ext import commands 
from discord.ext import tasks
from itertools import cycle

#my bot's command prefix
client = commands.Bot(command_prefix="g!")

#list of status here
status = cycle(['use "g!" as prefix, For Eg: -help', 'I wish I was Cool'])

#just a basic hi to hello event
@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    elif message.content.startswith("hi"):

        if str(message.author) == "CodePoltergeist#8379": 
            await message.channel.send("Hello " + str(message.author) + "!")
        else:
            await message.channel.send("Heya dude, Wassup?")

    elif str(message.channel) == "pictures" and message.content != "":
        await message.channel.purge(limit=1)

    else:
        await client.process_commands(message)

#this will show if someone leaves or joins, actually not so-helpful
@client.event
async def on_message_join(member):
    print(f'{member} has joined NGL we are very happy to have you!')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server, and its sed!')

@client.event
async def on_ready():
    change_status.start()

#the playing status.
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#for no command found errors
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Sorry there is no command as you just mentioned above')

#shows the internet ping or latency.
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

#a lucky or not game
@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#for server information (embed one)
@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = ctx.guild.icon_url

    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)

#clear message command
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

#clear message error
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('please also specify the amount of messages that should be deleted.')

#kick command
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

#ban command
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

#unban command
@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) ==(member_name, member_discriminator):
            await ctx.guild.unban(user)

        embed=discord.Embed(
            colour=discord.Colour.green()
        )

        embed.set_author(name='Unban member')
        embed.add_field(name=f'{user} has been successfully unbanned from this server', value='They can now join back with another invite')
        embed.set_footer(text=f'{user} was unbanned by {ctx.message.author.name}')
        await ctx.channel.send(embed=embed)
        return


client.run('NzQ3Njk3ODU1MTk5OTY5Mjgx.X0Sp5A.Q--ejtIyfw579qI6IJ4NDUsJX70')





