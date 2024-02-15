import asyncio
import discord
import config
from discord.ext import commands


channels_to_resend = ['└📢・выпуски', 'основной']
keyphrase_to_resend = 'Resend'
keymode = True

discord_intents = discord.Intents.default()
discord_intents.members = True
discord_intents.messages = True
discord_intents.message_content = True
bot = commands.Bot(command_prefix=config.prefix, intents=discord_intents)
bot.remove_command("help")


@bot.event
async def on_message(msg):
    try:
        if msg.channel.name in channels_to_resend and (keymode and keyphrase_to_resend in msg.content):
            images = [discord.Embed().set_image(url=msg.attachments[i].url) for i in range(len(msg.attachments))]
            for member in msg.guild.members:
                if not member.bot:
                    now = msg.embeds
                    embed = discord.Embed()
                    if now:
                        embed.add_field(name=' Новости PlayStrix', value=msg.content)
                        await member.send(embeds=[embed] + now)
                    else:
                        embed.add_field(name=' Новости PlayStrix', value=msg.content)
                        if len(images) == 1:
                            embed.set_image(url=msg.attachments[0].url)
                            await member.send(embed=embed)
                        else:
                            await member.send(embeds=[embed] + images)
    except Exception as e:
        pass


async def runner():
    await bot.start(token=config.token)


if __name__ == '__main__':
    asyncio.run(runner())
