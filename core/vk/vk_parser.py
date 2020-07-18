import json
from datetime import datetime

import vk
from decouple import config
from core.models import VKGroup, VKPost, VKSource


class VKParser:
    def __init__(self):
        self.session = vk.Session()
        self.api = vk.API(self.session)
        self.ACCESS_TOKEN = config('ACCESS_TOKEN')

    def parse_group(self, vk_id):
        response = self.api.groups.getById(access_token=self.ACCESS_TOKEN, v='5.35',
                                           lang='ru', group_ids=vk_id,
                                           fields='description,members_count,verified,site,cover')
        response = response[0]
        new_group = VKGroup(name=response['name'],
                            vk_id=response['id'],
                            description=response['description'],
                            members_count=response['members_count'],
                            verified=response['verified'],
                            site=response['site'],
                            photo_100=response['photo_100'])
        new_group.save()

    def parse_posts(self, source):
        response = self.api.wall.get(access_token=self.ACCESS_TOKEN, v='5.35',
                                     lang='ru', timeout=1000, owner_id='-' + str(source), count=50)
        posts = response['items']
        for post in posts:
            new_post = VKPost(owner_id=VKGroup.objects.get(vk_id=abs(post['owner_id'])),
                              pub_date=datetime.fromtimestamp(post['date']),
                              text=post['text'],
                              comments=post['comments']['count'],
                              likes=post['likes']['count'],
                              reposts=post['reposts']['count'],
                              checked=False
                              )
            new_post.save()

    def parse_groups(self):
        groups = VKSource.objects.values('vk_id').all()
        for group in groups:
            self.parse_group(group['vk_id'])
            self.parse_posts(group['vk_id'])
