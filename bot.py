import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from gtts import gTTS
from time import sleep
client = commands.Bot(command_prefix = '!')
@client.event
async def on_ready():
    print("Bot Online")
@client.command(pass_context = True)
async def translate(ctx, *, arg):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        tts = gTTS(arg)
        tts.save('/audio.mp3')                     #change to path of audio
        source = FFmpegPCMAudio('/audio.mp3')      #keep path same
        player = voice.play(source)
        sleep(5)
        await ctx.guild.voice_client.disconnect()

client.run('')                                         #bot token here  
