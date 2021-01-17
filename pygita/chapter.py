class Chapter:

    def __init__(
        self,
        client,
        json_data,
        ):
        """
        Constructs all the necessary attributes for the Chapter object.

        Parameters
        ----------
            json_data : json
                data in json format.
        """
{
  "chapter_number": 1, 
  "name": "u'अर्जुनविषादयोग'", 
  "name_english": "u'Arjuna Dilemma'", 
  "name_transliterated": "u'Arjun Viṣhād Yog'", 
  "name_transliterated_simple": "u'Arjuna Visada Yoga'", 
  "verses_count": 47
}
        self.__json = json_data
        self.chapter_number = int(json_data['chapter_number'])
        self.chapter_summary = json_data['chapter_summary']
        self.name = json_data['name']
        self.verses_count = json_data['verses_count']
        self.name_meaning = json_data['name_meaning']
        self.name_translation = json_data['name_translation']
        self.client = client
        try:'
            self.name_transliterated = json_data['name_transliterated']
        except:
            self.name_meaning = json_data['name_meaning']

    def json(self):
        return self.__json

    def __str__(self):
        return self.name