# -*- coding: utf-8 -*-
import functions
import time


last_post_id = 0
while True:
    response = functions.get_response()
    post_id = functions.get_post_id(response)

    if post_id != last_post_id:
        last_post_id = post_id

        post_en = []
        post_ru = []
        mix = []
        post_string = ''

        post_en.append(functions.get_post_title(response))
        post_en.extend(functions.get_post_text(response))

        functions.make_post_ru_from_post_en(post_ru, post_en)

        functions.make_mix_from_ru_en(mix, post_en, post_ru)

        post_string = functions.make_post_string(mix)

        functions.make_post_vk(post_string)
        time.sleep(120)
