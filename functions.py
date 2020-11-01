# -*- coding: utf-8 -*-
import fake_useragent
import requests
from nltk import tokenize
from googletrans import Translator

translator = Translator()


def get_response():
    user = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    link = 'https://www.reddit.com/r/tifu/new/.json'
    headers = {'user-agent': user}
    return requests.get(link, headers=headers)


def get_post_id(response):
    return response.json()['data']['children'][0]['data']['created_utc']


def get_post_title(response):
    return response.json()['data']['children'][0]['data']['title']


def get_post_text(response):
    return tokenize.sent_tokenize(response.json()['data']['children'][0]['data']['selftext'])


def make_post_ru_from_post_en(post_ru, post_en):
    for sentence in post_en:
        translated = translator.translate(sentence, dest='ru').text
        post_ru.append(translated)


def make_mix_from_ru_en(mix, post_en, post_ru):
    for j in range(len(post_en)):
        mix.append(post_en[j])
        mix.append(post_ru[j])


def make_post_string(mix):
    string = ''
    for i in range(len(mix)):
        string += mix[i]
        string += '\n\n'
    return string


def make_post_vk(text):
    data = {'access_token': "a312c2c4514b147e3f4099120995a99383d34a3cfa7d51ef7d4334d61e725a9d370a98d2a20b32b01769e",
            'owner_id': -199738353,
            'from_group': 1,
            'message': text,
            'signed': 0,
            'v': "5.52"}
    requests.post('https://api.vk.com/method/wall.post', data=data)