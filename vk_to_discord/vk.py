import json

import vk_api
from vk_api.longpoll import VkLongPoll
from vk_api.longpoll import VkEventType


vk_session = vk_api.VkApi(app_id=51671125, token=servise_key)
vk = vk_session.get_api()

wall = vk.wall.get(domain=domain, count=1)

def get_videos(items: dict):
    list = []
    try:
        video = f"https://vk.com/video{attachments[3]['video']['owner_id']}_{attachments[1]['video']['id']}"
    except:
        pass

items = wall['items'][0]
text = items['text']
attachments = items['attachments']
get_videos(attachments)
try:
    photo = attachments[0]['photo']['sizes'][4]['url']
    video = f"https://vk.com/video{attachments[3]['video']['owner_id']}_{attachments[1]['video']['id']}"
    print(video)

except:
    pass
