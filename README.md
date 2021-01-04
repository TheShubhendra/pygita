# pygita
pygita is a wrapper of [bhagavadgita.io](https://bhagavadgita.io) api for Python 3

![PyPI - License](https://img.shields.io/pypi/l/pygita)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pygita)
![GitHub last commit](https://img.shields.io/github/last-commit/TheShubhendra/pygita)
![Build Status](https://img.shields.io/github/workflow/status/TheShubhendra/pygita/Python%20package)
![Code quality](https://img.shields.io/scrutinizer/quality/g/TheShubhendra/pygita)

# Installation
Install it from pypi using pip
```
pip install pygita
```

# Authentication
- Register on [bhagavadgita.io](https://bhagavadgita.io)
- Create App
- Copy  Client Id and Client Secret 
- `python
pygita.auth(client_id,client_secret)
`

# Usage
  ### 1. Authentication using client_id and secret_id

   This function generate a new access_token

  ```python
pygita.auth(client_id, client_secret)
  ```
  -----------------------------------
  ### 2. Authentication using access_token

  If you have access_token, you don't need to generate a new one.
  
  ```python
pygita.auth_token(access_token)
  ````
  -----------------------------------
  ### 3. Get all chapters 
  
  ```python
chapter_list = pygita.get_chapter()
  ```
  -----------------------------------
  
  
  ### 4. Get a specific chapter
  ```python
chapter = pygita.get_chapter(chapter_number)
  ```
  -----------------------------------
  
  ### 5. Get all Verses from all chapters
  
  ```python
list_of_all_verses = pygita.get_verse()
  ```
  -----------------------------------
  
  ### 6. Get all Verses from a specific chapter
  ```python
verses = pygita.get_verse(chapter_number=chapter_number)
  ```
  -----------------------------------
  ### 7. Get a specific verse from a specific chapter
  ```python
verse = pygita.get_verse(chapter_number=chapter_number,verse_number=verse_number)
  ```
 -----------------------------------
# Language
  English is the default language .To get verse or chapter in hindi pass language parameter with value of "hi" 
  
  ```python
  verse = pygita.get_verse(chapter_number=1,verse_number=1,language="hi")
  verse = pygita.get_chapter(chapter_number=1,language="hi")
  ```
# Classes
 Above functions from point 3 to 4 returns a object of the `Chapter` class and from point 5 to 7 returns a object of the `Verse` class
# Objects
  ## Attributes of **Chapter** objects
    1. chapter_number
    2. chapter_summary
    3. name
    4. verses_count
    5. name_meaning
    6. name_translation
    7. name_transliterated(in English only)
    8. name_meaning(in Hindi only)
  ## Methods of **Chapter** objects
    1. next() : returns object of next chapter
    2. previous() : returns object of previous chapter
    3. verse() : returns object of verse in that chapter if verse_number is passed . Otherwise it returns the list of all verses in that chapter.
    4. json() : returns above attributes in dictionary or json format
   
-----------------------------------
  ## Attributes of **Verse** objects
    1. chapter_number
    2. verse_number
    3. text
    4. meaning
    5. transliteration
    6. word_meanings
  ## Methods of **Verse** objects
    1. next() : returns object of next verse
    2. previous() : returns object of previous verse
    3. chapter() : returns the object of it's chapter
    4. json() : returns above attributes in dictionary or json format
