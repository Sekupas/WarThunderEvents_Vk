import random

import nextcord
from nextcord.ext import commands
from copy import deepcopy
from cfg import TOKEN
from vk import get_all

all = get_all()

url_post, text_post, photo = all[0], all[1], all[2]
if len(all) == 4:
    video = all[3]

TOKEN = TOKEN

intents = nextcord.Intents.all()
intents.members = True
intents.typing = True
intents.message_content = True
intents.presences = True

activity = nextcord.Activity(type=nextcord.ActivityType.listening, name="Музычку")
bot = commands.Bot(command_prefix='>>>', intents=intents, activity=activity, status=nextcord.Status.online)

avatar_author = 'https://sun9-24.userapi.com/impg/S0g9s8KKftuqPX3dIBHHY2jw8tgGtnC4x-i9Jg/azI1ProULmg.jpg?size=512x512&quality=95&sign=c5ee033441f41cf2ac4e2d057f6d2df6&type=album'
channel_id = 1109839451200438372

embed_main = nextcord.Embed.from_dict({
    "description": text_post,
    "url": photo[0],
    "color": 0xE74C3C,
    "author": {
        "name": "War Thunder Events",
        "url": 'https://vk.com/warthunderevents',
        "icon_url": avatar_author
    },
    "image": {
        "url": photo[0]
    },
})




@bot.event
async def on_ready():
    auth = f'Авторизован как {bot.user} (ID: {bot.user.id})'
    print('+', '-' * len(auth), '+')
    print('|', auth, '|')
    print('+', '-'*len(auth), '+')

@bot.event
async def on_ready():
    channel = bot.get_channel(channel_id)

    try:
        embed1 = nextcord.Embed()
        embed1.url = photo[1]
        embed1.set_image(photo[1])

        embed2 = nextcord.Embed()
        embed2.url = photo[2]
        embed2.set_image(photo[2])
        await channel.send(embeds=[embed1, embed2])
    except:
        try:
            embed1 = nextcord.Embed()
            embed1.url = photo[1]
            embed1.set_image(photo[1])
            await channel.send(embed=embed1)
        except:
            await channel.send(embed=embed_main)










bot.run(TOKEN)