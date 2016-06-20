import json
from urllib import request

ID_API = 'https://www.wikidata.org/w/api.php?action=wbgetentities'


class JsonParse:
    def __init__(self, url):
        self.url = url
        self.__json_dir = self.__request(url)
        self.__json_id = ''
        self.__json_title = ''

    def __request(self,url):
        with request.urlopen(url) as f:
            json_req = f.read().decode('utf-8')
            return json.loads(json_req)

    def __get_basic(self, json_dir):
        basic = []
        for k in json_dir['entities']:
            basic.append(json_dir['entities'][k]['id'])
            if 'en' in json_dir['entities'][k]['labels']:
                basic.append(json_dir['entities'][k]['labels']['en']['value'])
            else:
                basic.append('None')
            if 'en' in json_dir['entities'][k]['descriptions']:
                basic.append(json_dir['entities'][k]['descriptions']['en']['value'])
            else:
                basic.append('None')
        return basic

    def __new_entity(self,entity_id):
        url = ID_API + '&ids=' + entity_id + '&format=json&languages=en'
        return self.__request(url)

    def get_entities(self):
        entities = []
        for k in self.__json_dir['search']:
            if 'description' in k:
                entity = [k['id'], k['label'], k['description']]
            else:
                entity = [k['id'], k['label'], 'None']
            entities.append(entity)
        return entities

    def get_detail(self):
        print("Searching.....")
        details = []
        for k in self.__json_dir['entities']:
            basic = []
            basic.append(self.__json_dir['entities'][k]['id'])
            if 'en' in self.__json_dir['entities'][k]['labels']:
                basic.append(self.__json_dir['entities'][k]['labels']['en']['value'])
            else:
                basic.append('None')
            if 'en' in self.__json_dir['entities'][k]['descriptions']:
                basic.append(self.__json_dir['entities'][k]['descriptions']['en']['value'])
            else:
                basic.append('None')
            details.append(basic)
            for i in self.__json_dir['entities'][k]['claims']:
                detail = []
                predicate_dir = self.__new_entity(i)
                predicate_info = self.__get_basic(predicate_dir)
                detail.append(i)
                detail.append(predicate_info[1])
                claims_id = []
                claims_title = []
                claims_description = []
                for j in self.__json_dir['entities'][k]['claims'][i]:
                    if j['mainsnak']['datavalue']['type'] == 'wikibase-entityid':
                        if j['mainsnak']['datavalue']['value']['entity-type'] == 'item':
                            item_id = 'Q' + str(j['mainsnak']['datavalue']['value']['numeric-id'])
                        else:
                            print(j['mainsnak']['datavalue']['value']['entity-type'])
                            return
                        claims_id.append(item_id)
                        item_dir = self.__new_entity(item_id)
                        item_info = self.__get_basic(item_dir)
                        claims_title.append(item_info[1])
                        claims_description.append(item_info[2])
                    else:
                        claims_id.append('Value')
                        claims_title.append(j['mainsnak']['datavalue']['value'])
                        # claims_description.append(None)
                detail.append(claims_id)
                detail.append(claims_title)
                detail.append(claims_description)
                print(detail)
                details.append(detail)
        print("Search Done")
        print(details)
        return details
