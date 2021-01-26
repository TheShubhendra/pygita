#!/usr/bin/python
# -*- coding: utf-8 -*-


class Verse:
    def __init__(
        self,
        client,
        json_data,
    ):
        """
        Constructs all the necessary attributes for the Verse object.

        Parameters
        ----------
            json_data : json
                data in json format
        """

        self.__json = json_data
        self.text = json_data["text"]
        self.meaning = json_data["meaning"]
        self.transliteration = json_data["transliteration"]
        self.chapter_number = int(json_data["chapter_number"])
        self.verse_number = int(json_data["verse_number"])
        self.word_meanings = json_data["word_meanings"]
        self.client = client

    def json(self):
        return self.__json

    def __str__(self):
        return self.text
