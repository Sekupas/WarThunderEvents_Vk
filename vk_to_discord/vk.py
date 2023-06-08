import json

import vk_api
from vk_api.longpoll import VkLongPoll
from vk_api.longpoll import VkEventType
from cfg import servise_key, domain

vk_session = vk_api.VkApi(app_id=51671125, token=servise_key)
vk = vk_session.get_api()

wall = vk.wall.get(domain=domain, count=1)

def get_videos(items: dict):
    list = []
    length = len(items)
    for number in range(length):
        try:
            video = f"https://vk.com/video{items[1]['video']['owner_id']}_{items[number]['video']['id']}"
            list.append(video)
        except:
            pass
    return list



def get_all():
    try:
        items = wall['items'][0]
        # print(items['owner_id'], items['post_id'])
        text = items['text']
        text = f"`{text}`"


        attachments = items['attachments']
        url = f"https://vk.com/wall{wall['items'][-1]['owner_id']}_{wall['items'][-1]['id']}"
        photo = attachments[0]['photo']['sizes'][4]['url']
        videos = get_videos(attachments)
        return url, text, videos, photo
    except Exception as e:
        return e