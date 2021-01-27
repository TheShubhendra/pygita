# pygita

pygita is a wrapper of [bhagavadgita.io](https://bhagavadgita.io) api for Python 3


![PyPI - License](https://img.shields.io/pypi/l/pygita)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pygita)
![GitHub last commit](https://img.shields.io/github/last-commit/TheShubhendra/pygita)
![Build Status](https://img.shields.io/github/workflow/status/TheShubhendra/pygita/Python%20package)
![Code quality](https://img.shields.io/scrutinizer/quality/g/TheShubhendra/pygita)
![Scrutinizer coverage](https://img.shields.io/scrutinizer/coverage/g/TheShubhendra/pygita)
![Requires.io (branch)](https://img.shields.io/requires/github/TheShubhendra/pygita/master)
![GitHub repo size](https://img.shields.io/github/repo-size/TheShubhendra/pygita)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pygita)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/pygita)
![PyPI](https://img.shields.io/pypi/v/pygita)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![PyPI - Status](https://img.shields.io/pypi/status/pygita)
![PyPI - Format](https://img.shields.io/pypi/format/pygita)

## Installation
Install it from pypi using pip
```bash
pip install pygita
```

## Authentication

- Register on [bhagavadgita.io](https://bhagavadgita.io)
  
- Create App
 
- Copy  Client Id and Client Secret 
  

## Usage
  ### 1. Create a client

   ```python
   from pygita import Client
   client = Client(CLIENT_ID, CLIENT_SECRET)
   ```
  ### 2. Get a verse
  ```python
  verse = client.get_verse(verse_number, chapter_number)
  ```
  
  ### 3. Get a chapter
  ```python
  chapter = client.get_chapter(chapter_number)
  ```
 -----------------------------------

### Objects
  #### Attributes of **Chapter** objects
    1. chapter_number
    2. chapter_summary
    3. name
    4. verses_count
    5. name_meaning
    6. name_translation
    7. name_transliterated(in English only)
    8. name_meaning(in Hindi only)

-----------------------------------
  #### Attributes of **Verse** objects
    1. chapter_number
    2. verse_number
    3. text
    4. meaning
    5. transliteration
    6. word_meanings
