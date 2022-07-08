import discord
from discord.ext.commands import Bot
import emoji

#Python Version: 3.10.0
#Version: 0.0.5

def char_is_emoji(char):
    return char in emoji.EMOJI_DATA

bot = Bot('---')

#vvv Bot Events vvv
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=str("Looking for non-english")))
    print('Bot is online as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    for i in list(message.content):
        char = ord(i)
        if char > 127462 and char < 127487: #Regonial identifiers. used for flags
            break
        if char < 0 or char > 127 and not char_is_emoji(i): #Unicode latin alphabet range
            await message.delete() #removes message
            return
#^^^Bot Events ^^^


bot.run('') #token to connect to discord.
