import json

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
                                           lang='ru', group_id=vk_id,
                                           fields='description,members_count,verified,site,cover')
        json.loads(response)
        # todo: json serialization and writing to db

    def parse_posts(self, source):
        self.api.wall.get(access_token=self.ACCESS_TOKEN, v='5.35',
                          lang='ru', timeout=1000, owner_id=str(source), count=50)
        # todo: json serialization and writing to db

    def parse_groups(self):
        groups = VKSource.objects.values('vk_id').all()
        for group in groups:
            self.parse_group(group['vk_id'])
            self.parse_posts(group['vk_id'])
