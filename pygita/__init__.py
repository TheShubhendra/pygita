#!/usr/bin/python
# -*- coding: utf-8 -*-

from requests import post, get
import datetime
from pygita.utils import generate_token
from pygita.constants import TOTAL_CHAPTERS, TOTAL_VERSES, VERSE_COUNT, \
    ERROR_MESSAGE, TOKEN_VALIDITY


class Token:

    def __init__(self):
        pass


class Client:

    def __init__(
        self,
        client_id,
        client_secret,
        grant_type='client_credentials',
        scope='verse chapter',
        ):

        self.client_id = client_id
        self.client_secret = client_secret
        self.token = Token()
        self.token.grant_type = grant_type
        self.token.scope = scope
        self.token.value = generate_token(client_id, client_secret,
                grant_type, scope)
        self.client = self
        self.token.expiry = datetime.datetime.now() \
            + datetime.timedelta(seconds=TOKEN_VALIDITY)

    def _re_authenticate(self):
        self.token.value = generate_token(self.client_id,
                self.client_secret, self.token.grant_type,
                self.token.scope)
        self.token.expiry = datetime.datetime.now() \
            + datetime.timedelta(seconds=TOKEN_VALIDITY)

    def _get_token(self):
        if datetime.datetime.now() >= self.token.expiry:
            self._re_authenticate()
        return self.token.value

    def get_chapter(self, chapter_number, language='en'):
        token = self.token.value
        if language == 'hi':
            url = \
                '''https://bhagavadgita.io/api/v1/chapters\
/{chapter_number}?access_token={token}&\
language=hi'''.format(chapter_number=chapter_number,
                    token=token)
        else:
            url = \
                '''https://bhagavadgita.io/api/v1/chapters\
/{chapter_number}?access_token={token}\
'''.format(chapter_number=chapter_number,
                    token=token)
        request = get(url)
        if request.status_code == 200:
            response = request.json()
        return Chapter(self, response, language)

    def get_verse(
        self,
        chapter_number=None,
        verse_number=None,
        language='en',
        ):
        token = self._get_token()
        if verse_number is None and chapter_number is None:
            return Verse.all(language=language)
        elif verse_number is None:
            return Verse.all(chapter_number, language=language)
        elif chapter_number is None:
            pass
        else:
            if language == 'hi':
                url = \
                    '''https://bhagavadgita.io/api/v1/chapters\
/{chapter_number}/verses/{verse_number}\
?access_token={token}&language={language}'''.format(chapter_number=chapter_number,
                        verse_number=verse_number,
                        token=token,
                        language=language,
                        )
            else:
                url = \
                    '''https://bhagavadgita.io/api/v1/chapters/{chapter_number}/verses/{verse_number}\
?access_token={token}'''.format(chapter_number=chapter_number,
                        verse_number=verse_number, token=token)
            request = get(url)
            response = request.json()
            return Verse(client=self, json_data=response,
                         language=language)


class Chapter:

    def __init__(
        self,
        client,
        json_data,
        language='en',
        ):
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
        self.chapter_number = int(json_data['chapter_number'])
        self.chapter_summary = json_data['chapter_summary']
        self.name = json_data['name']
        self.verses_count = json_data['verses_count']
        self.name_meaning = json_data['name_meaning']
        self.name_translation = json_data['name_translation']
        self.client = client
        if language == 'en':
            self.name_transliterated = json_data['name_transliterated']
        else:
            self.name_meaning = json_data['name_meaning']

    def next(self):
        chapter_number = self.chapter_number
        if chapter_number >= 18:
            return 'No chapter'
        return self.client.get_chapter(int(chapter_number) + 1,
                language=self.language)

    def previous(self):
        chapter_number = self.chapter_number
        if chapter_number <= 1:
            return 'No chapter'
        return self.client.get_chapter(int(chapter_number) - 1,
                language=self.language)

    def json(self):
        return self.__json

    def verse(self, verse_number=None):
        if verse_number is None:
            return self.all()
        else:
            return self.client.get_verse(chapter_number=self.chapter_number,language=self.language)

    def all(self, language='en'):
        token = self._get_token()
        if language == 'hi':
            url = \
                '''https://bhagavadgita.io/api/v1/chapters?
access_token={token}'''.format(token=token)
        else:
            url = \
                '''https://bhagavadgita.io/api/v1/chapters?\
                   access_token={token}& language=hi'''.format(token=token)
        request = get(url)
        response = request.json()
        return [Chapter(json_data, language=language) for json_data in
                response]


class Verse:

    def __init__(
        self,
        client,
        json_data,
        language='en',
        ):
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
        self.text = json_data['text']
        self.meaning = json_data['meaning']
        self.transliteration = json_data['transliteration']
        self.chapter_number = int(json_data['chapter_number'])
        self.verse_number = int(json_data['verse_number'])
        self.word_meanings = json_data['word_meanings']
        self.client = client

    def next(self):
        chapter_number = self.chapter_number
        verse_number = self.verse_number
        return self.client.get_verse(chapter_number=chapter_number,
                verse_number=int(verse_number) + 1,
                language=self.language)

    def previous(self):
        chapter_number = self.chapter_number
        verse_number = self.verse_number
        return self.client.get_verse(int(verse_number) - 1,
                chapter_number, language=self.language)

    def json(self):
        return self.__json

    def chapter(self):
        return self.client.get_chapter(self.chapter_number,
                language=self.language)

    def all(self, chapter_number=None, language='en'):
        token = self._get_token()
        if chapter_number is None:
            url = \
                '''https://bhagavadgita.io/api/v1/verses?
            access_token={token}'''.format(token=token)
        else:
            url = \
                '''https://bhagavadgita.io/api/v1/chapters/{chapter_number}/verses?
            access_token={token}
            '''.format(chapter_number=chapter_number,
                    token=token)
        if language == 'en':
            url += '&language=hi'
        request = get(url)
        response = request.json()
        return [Verse(json_data, self.client, language=language)
                for json_data in response]