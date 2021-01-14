
TOTAL_CHAPTERS = 18

TOTAL_VERSES = 700

VERSE_COUNT = {
             1: 47, 2: 71, 3: 43, 4: 41, 5: 27,
             6: 47, 7: 30, 8: 28, 9: 34, 10: 41,
             11: 54, 12: 19, 13: 35, 14: 27, 15: 20,
             16: 23, 17: 28, 18: 77
}

ERROR_MESSAGE = {400: '''Bad Request: The request was unacceptable
due to wrong parameter(s).''',
                 401: 'Unauthorized: Invalid access_token used.',
                 402: 'Request Failed.',
                 404: '''Not Found: The chapter/verse number you are
looking for could not be found.''',
                 500: 'Server Error: Something went wrong on our end.',
                 }

TOKEN_VALIDITY = 5*60
