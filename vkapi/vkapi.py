from my_token import TOKEN_VK
import requests
from pprint import pprint
import time
import pandas as pd



# URL = 'https://api.vk.com/method/users.get'


# params = {
#     'user_ids': '1',
#     'access_token': TOKEN_VK,
#     'v':'5.131'
#     }
# res = requests.get(URL, params=params)
# pprint(res.json())

# params = {
#     'user_ids': '1, 20',
#     'access_token': TOKEN_VK,
#     'v':'5.131',
#     'fields': 'sex, education, books'
#     }
# res = requests.get(URL, params=params)
# pprint(res.json())

# Напишем функцию, которая будет находить группы по поисковому запросу при помощи метода groups.search
# def search_groups(q, sorting=0):
#     '''
#     Параметры sort
#     0 - сортировать по умолчанию
#     6 - сортировать по количеству пользователей
#     '''
#     params = {
#         'q': q,
#         'access_token': TOKEN_VK,
#         'v': '5.131',
#         'sort': sorting,
#         'count': 300
#     }
#     req = requests.get('https://api.vk.com/method/groups.search', params).json()
#     # pprint(req)
#     req = req['response']['items']
#     return req
#
#
# target_groups = search_groups('python')
#
#
# pprint(target_groups)
#
# # Получим расширенную информацию по группам при помощи метода groups.getById
# target_group_id = ','.join([str(group['name']) for group in target_groups])
# pprint(target_group_id)


# Строим сложную логику взаимодействия с API, инкапсулируем весь нужный функционал в класс.
# Какие нам нужны данные, чтобы инициализировать класс?

class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.params = {'access_token': token,
                       'v': version
                       }
#
#     # переносим в класс ранее написанный функционал
#
    def search_groups(self, q, sorting=0):
        '''
        Параметры sort
        0 - сортировать по умолчанию
        6 - сортировать по количеству пользователей
        '''
        group_search_url = self.url + 'groups.search'
        group_search_params = {
            'q': q,
            'sort': sorting,
            'count': 300
        }
        req = requests.get(group_search_url, params={**self.params, **group_search_params}).json()
        # pprint(req)
        return req['response']['items']
#
    def search_groups_ext(self, q, sorting=0):
        group_search_ext_url = self.url + 'groups.getById'
        target_groups = self.search_groups(q, sorting)
        target_group_ids = ','.join([str(group['id']) for group in target_groups])
        groups_info_params = {
            'group_ids': target_group_ids,
            'fields': 'activity, description'
        }
        req = requests.get(group_search_ext_url, params={**self.params, **groups_info_params}).json()
#         # pprint(req)

        return req['response']
#
    def get_followers(self, user_id=1):
        followers_url = self.url + 'users.getFollowers'
        followers_params = {
            'count': 1000,
            'user_id': user_id
            }
        req = requests.get(followers_url, params={**self.params, **followers_params}).json()

        return req['response']

    def get_groups(self, user_id=1):
        groups_url = self.url + 'groups.get'
        groups_params = {
            'count': 1000,
            'user_id': user_id,
            'extended': 1,
            'fields': 'members_count'
            }
        req = requests.get(groups_url, params={**self.params, **groups_params})
        # pprint(req)

        return req.json()


vk_client = VkUser(TOKEN_VK, '5.131')

# pprint(vk_client.search_groups('python'))
# pprint(vk_client.search_groups_ext('python'))
# pprint(vk_client.get_followers())
pprint(vk_client.get_groups())

