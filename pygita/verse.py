import os
from requests import get


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
