#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from requests import post, get
from utils import generate_token
from constants import (TOTAL CHAPTERS,
                       TOTAL_VERSES,
                       VERSE_COUNT,
                       ERROR_MESSAGE,
                       TOKEN_VALIDITY,
                       )


class Client:

    def __init__(self, client_id, client_secret, grant_type='client_credentials', scope='verse chapter'):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = generate_token(client_id, client_secret, grant_type, scope)
       self.expiry = datetime.datetime.now() + TOKEN_VALIDITY
    def _re_authenticate(self):
        self.token = generate_token(client_id, client_secret, grant_type, scope)
        self.expiry = datetime.datetime.now() + TOKEN_VALIDITY

    def _get_token(self):
        if datetime.datetime.now() >= self.expiry:
            self._re_authenticate()
        return self.token

    def get_chapter(self, chapter_number, language='en'):
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
        return Chapter(response, language)

    def get_verse(self, chapter_number=None, verse_number=None, language='en'):
    token = self._get_token()
    if verse_number is None and chapter_number is None:
        return Verse.all(language=language)
    elif verse_number is None:
        return Verse.all(chapter_number, language=language)
    elif chapter_number is None:
        pass'
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


class Chapter:

    def __init__(self, json_data, language='en'):

        """
        Constructs all the necessary attributes for the Chapter object.

        Parameters
        ----------
            json_data : json
                data in json format
            language : str
                language hi/en
        """
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

    def all(self, language='en'):
        token = self._get_token()
        if language == 'hi':
            url = \
                ''''https://bhagavadgita.io/api/v1/chapters?access_token={token}
                '''.format(token=token
        else:
            url = \
                '''https://bhagavadgita.io/api/v1/chapters?access_token={token}& language=hi
                '''.format(token=token)

        request = get(url)
        if request.status_code == 200:
            response = request.json()
        else:
            print(message[request.status_code])
            return
        return [Chapter(json_data, language=language) for json_data in
                response]


class Verse:
    def __init__(self, json_data, language="en"):
        """
        Constructs all the necessary attributes for the Verse object.

        Parameters
        ----------
            json_data : json
                data in json format
            language : str
                language hi/en
        """        
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

    def all(self, chapter_number=None, language="en"):
        token = self._get_token()
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
