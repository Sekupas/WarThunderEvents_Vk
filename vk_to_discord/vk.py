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

def get_number_res(items: list):
    count = len(items)
    for number in range(count):
        type = items[number]['type']
        if type == 'x':
            photo_url = items[number]['url']
            return photo_url
    return items[0]['width']
def get_photos(items: dict):
    list = []
    length = len(items)
    for number in range(length):
        try:
            photo = get_number_res(items[number]['photo']['sizes'])
            list.append(photo)
        except:
            pass
    return list


def get_all():
    try:
        items = wall['items'][0]
        # print(items['owner_id'], items['post_id'])
        text = items['text']
        text = f"*{text}*"


        attachments = items['attachments']
        url = f"https://vk.com/wall{wall['items'][-1]['owner_id']}_{wall['items'][-1]['id']}"
        photo = get_photos(attachments)
        videos = get_videos(attachments)
        if len(photo) > 0 and len(videos) > 0:
            return url, text, videos, photo
        elif len(photo) > 0 :
            return url, text, photo
        else:
            return url, text, videos
    except Exception as e:
        return e