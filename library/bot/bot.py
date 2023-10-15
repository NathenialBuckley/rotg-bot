import discord
from discord import Embed
from discord.ext import commands
import random
import os


# Bot will have access to all Gateway Intents and Functions.
intents = discord.Intents.all()
intents.message_content = True

client = commands.Bot(  # Bot Prefix Begin
    command_prefix=commands.when_mentioned_or('!'), intents=intents
)


async def get_prefix(bot, message):
    prefixes_for = []
    extras = await prefixes_for(message.guild)  # returns a list
    return commands.when_mentioned_or(*extras)(bot, message)

# Bot Prefix End


@client.event
async def on_ready():
    # SUFFFFEERRRR!!!!
    print(f'=================\nMAKE THEM SUFFER!\n=================')


@client.command(aliases=['p'])  # Ping Pong Start
async def ping(ctx):
    await ctx.send('Pong!')
# Ping Pong End


@client.command()  # Kick Command Start
async def kick(ctx, member: discord.Member, *, reason=None):
    if not ctx.author.guild_permissions.kick_members:
        await ctx.send('You do not have the power to wield me!')
        return
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked.')


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please provide a user.')

# Kick Command End


@client.command()  # Ban Command Start
async def ban(ctx, member: discord.Member, *, reason=None):
    if (not ctx.author.guild_permissions.ban_members):
        await ctx.send('You do not have the power to wield me!')
        return
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned.')


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please provide a user.')

# Ban Command End


@client.command()  # Unban Command Start
async def unban(ctx, *, member):
    if (not ctx.author.guild_permissions.ban_members):
        await ctx.send('You do not have the power to wield me!')
        return
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mentioned}')
            return

# Unban Command End


@client.command(aliases=['purge'])  # Delete Messages Command Start
async def clear(ctx, amount=11):
    if (not ctx.author.guild_permissions.manage_messages):
        await ctx.send('You do not have the power to wield me!')
        return
    amount = amount+1
    if amount > 101:
        await ctx.send('I can not delete that many messages.')
    else:
        await ctx.channel.purge(limit=amount)
        await ctx.send('Cleared Messages')

# Delete Messages Command End

TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
