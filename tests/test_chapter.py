from .data import chapter_7_en

def test_specific_chapter(client):
    chapter = client.get_chapter(7)
    assert chapter.chapter_number == chapter_7_en["chapter_number"]
    assert chapter.chapter_summary == chapter_7_en["chapter_summary"]
    assert chapter.name == chapter_7_en["name"]
    assert chapter.name_translation == chapter_7_en["name_translation"]
    assert chapter.name_transliterated == chapter_7_en["name_transliterated"]
    assert chapter.verses_count == chapter_7_en["verses_count"]
    assert chapter.json() == chapter_7_en
    assert str(chapter) == chapter_7_en["name"]