import os
from requests import get


class Chapter:
    def __init__(self, json_data, language='en'):
        self.language = language
        self.__json = json_data
        self.chapter_number = json_data['chapter_number']
        self.chapter_summary = json_data['chapter_summary']
        self.name = json_data['name']
        self.verses_count = json_data['verses_count']
        self.name_meaning = json_data['name_meaning']
        self.name_translation = json_data['name_translation']
        if language == 'en':
            self.name_transliterated = json_data['name_transliterated']
        else:
            self.name_meaning = json_data['name_meaning']

    def next(self):
        chapter_number = self.chapter_number
        if chapter_number >= 18:
            return 'No chapter'
        return get_chapter(int(chapter_number) + 1,
                           language=self.language)

    def previous(self):
        chapter_number = self.chapter_number
        if chapter_number <= 1:
            return 'No chapter'
        return get_chapter(int(chapter_number) - 1,
                           language=self.language)

    def json(self):
        return self.__json

    def verse(self, verse_number=None):
        if verse_number is None:
            return Verse.all(self.chapter_number,
                             language=self.language)
        else:
            return get_verse(self.chapter_number, verse_number,
                             language=self.language)

    @classmethod
    def all(cls, language='en'):
        if language == 'hi':
            url = \
                ''''https://bhagavadgita.io/api/v1/chapters?access_token={token}
                '''.format(token=os.environ.get('gita_access_token'))
        else:
            url = \
                '''https://bhagavadgita.io/api/v1/chapters?access_token={token}& language=hi
                '''.format(token=os.environ.get('gita_access_token'))

         request = get(url)
        if request.status_code == 200:
            response = request.json()
        else:
            print message[request.status_code]
            return
        return [Chapter(json_data, language=language) for json_data in
                response]