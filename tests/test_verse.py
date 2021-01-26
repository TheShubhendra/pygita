from .data import verse_7_7_en

#                   verse_14_20_hi,
#                  )


def test_specific_verse(client):
    verse_en = client.get_verse(7, 7)
    #    verse_hi = client.get_verse(14,20,"hi")
    assert verse_en.chapter_number == verse_7_7_en["chapter_number"]
    assert verse_en.meaning == verse_7_7_en["meaning"]
    assert verse_en.text == verse_7_7_en["text"]
    assert verse_en.transliteration == verse_7_7_en["transliteration"]
    assert verse_en.verse_number == verse_7_7_en["verse_number"]
    assert verse_en.word_meaning == verse_7_7_en["word_meaning"]


#    assert verse_hi.json() == verse_14_20_hi


# def test_verse_methods(client, verse):
#     next_verse = verse.next()
#     assert next_verse.verse_number == 6
#     assert next_verse.chapter_number == 4

#     prev_verse = verse.previous()
#     assert prev_verse.verse_number == 4
#     assert prev_verse.chapter_number == 4


# def test_chapter_method(client, verse, chapter):
#     verse_chapter = verse.chapter()
#     assert verse_chapter.__dict__ == chapter.__dict__


# def all_verse_method(client, verse):
#     all_verse = verse.all()
#     assert type(all_verse) == list
#     assert len(all_verse) == 500
#     assert all_verse[0].verse_number == 1
#     assert all_verse[1].chapter_number == 1
