import discord

from discord.ext import commands

prefix = ''
token  = ''

bot = commands.Bot(command_prefix=prefix, help_command=None, intents=discord.Intents.all())

@bot.command()
@commands.has_permissions(administrator=True)
async def get(ctx):

    bans = await ctx.guild.bans()
    for ban in bans:
        userID = ban.user.id
        await ctx.send(userID)
        Userobject = await bot.fetch_user(userID)
        await ctx.guild.unban(Userobject)


bot.run(token)
