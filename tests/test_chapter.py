from .data import (chapter_7_en,
                   chapter_14_hi,
                  )


def test_specific_chapte(client):
    chapter_en = client.get_chapter(7)
    chapter_hi = client.get_chapter(14,"hi")
    assert chapter_en.json() == chapter_7_en
    assert chapter_hi.json() == chapter_14_hi


def test_chapter_methods(client, chapter):
    next_chapter = chapter.next()
    assert next_chapter.chapter_number == 5
    
    prev_chapter = chapter.previous()
    assert prev_chapter.chapter_number == 3


def test_chapter_method(client, verse, chapter):
    verse_chapter = verse.chapter()
    assert verse_chapter.__dict__ == chapter.__dict__


def test_verse_method(client, verse, chapter):
    assert chapter.verse(5).__dict__ == verse.__dict__
    all_verses = chapter.verse()
    assert type(all_verses) == list
    assert len(all_verses) == 5
    assert all_verses[4].__dict__ == verse.__dict__