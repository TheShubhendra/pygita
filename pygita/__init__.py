#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from requests import post, get

message = {400: '''Bad Request: The request was unacceptable
due to wrong parameter(s).''',

           401: 'Unauthorized: Invalid access_token used.',
           402: 'Request Failed.',
           404: '''Not Found: The chapter/verse number you are
           looking for could not be found.''',
           500: 'Server Error: Something went wrong on our end.',
           }


# Authentication from access_token
def auth_token(token):
    os.environ['gita_access_token'] = token


# Authentication from client_id and client_secret
def auth(client_id, client_secret):
    request = post('https://bhagavadgita.io/auth/oauth/token',
                   data={
                         'client_id': client_id,
                         'client_secret': client_secret,
                         'grant_type': 'client_credentials',
                         'scope': 'verse chapter',
                          })
    token = request.json()['access_token']
    os.environ['gita_access_token'] = token
    return 'You are authenticated by the generated token ' + token


def get_chapter(chapter_number=None, language='en'):
    if chapter_number is None:

        return Chapter.all()
    else:
        token = os.environ.get('gita_access_token')
        if language == 'hi':
            url = \
                '''https://bhagavadgita.io/api/v1/chapters/{chapter_number}?
                access_token={token}&language=hi
                '''.format(chapter_number=chapter_number,
                           token=token)
        else:
            url = \
                '''https://bhagavadgita.io/api/v1/chapters/{chapter_number}?
                access_token={token}
                '''.format(chapter_number=chapter_number,
                           token=token)
        request = get(url)
        if request.status_code == 200:
            response = request.json()
        else:
            print(message[request.status_code])
            return
        return Chapter(response, language)


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
            print(message[request.status_code])
            return
        return [Chapter(json_data, language=language) for json_data in
                response]


def get_verse(chapter_number=None, verse_number=None, language='en'):
    token = os.environ.get('gita_access_token')
    if token is None:
        print('Authentication not done')
        return
    if verse_number is None and chapter_number is None:
        return Verse.all(language=language)
    elif verse_number is None:
        return Verse.all(chapter_number, language=language)
    elif chapter_number is None:

        print('Please pass enough arguments')
    else:
        if language == 'hi':
            url = \
                '''https://bhagavadgita.io/api/v1/chapters/{chapter_number}/verses/{verse_number}
                ?access_token={token}&language={language}
                '''.format(chapter_number=chapter_number,
                           verse_number=verse_number, language=language,
                           token=token)
        else:
            url = \
                '''https://bhagavadgita.io/api/v1/chapters/{chapter_number}/verses/{verse_number}
                ?access_token={token}
                '''.format(chapter_number=chapter_number,
                           verse_number=verse_number,
                           token=token)
        request = get(url)
        if request.status_code == 200:
            response = request.json()
        else:
            print(message[request.status_code])
            return
        return Verse(json_data=response, language=language)


class Verse:
    def __init__(self, json_data, language="en"):
        self.language = language
        self.__json = json_data
        self.text = json_data["text"]
        self.meaning = json_data["meaning"]
        self.transliteration = json_data["transliteration"]
        self.chapter_number = json_data["chapter_number"]
        self.verse_number = json_data["verse_number"]
        self.word_meanings = json_data["word_meanings"]

    def next(self):
        chapter_number = self.chapter_number
        verse_number = self.verse_number
        return get_verse(chapter_number=chapter_number,
                         verse_number=int(verse_number)+1,
                         language=self.language,
                         )

    def previous(self):
        chapter_number = self.chapter_number
        verse_number = self.verse_number
        return get_verse(int(verse_number)-1,
                         chapter_number,
                         language=self.language,
                         )

    def json(self):
        return self.__json

    def chapter(self):
        return get_chapter(self.chapter_number, language=self.language)

    @classmethod
    def all(cls, chapter_number=None, language="en"):
        token = os.environ.get("gita_access_token")
        if chapter_number is None:
            url = """https://bhagavadgita.io/api/v1/verses?
            access_token={token}""".format(token=token)
        else:
            url = """https://bhagavadgita.io/api/v1/chapters/{chapter_number}/verses?
            access_token={token}
            """.format(chapter_number=chapter_number,
                       token=token,
                       )
        if language == "hi":
            url += "&language=hi"
        if token is None:
            print("Authentication not done")
            return
        request = get(url)
        if request.status_code == 200:
            response = request.json()
        else:
            return
        return [Verse(json_data, language=language) for json_data in response]
