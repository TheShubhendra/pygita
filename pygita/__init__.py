from requests import get, post
import os
from verse import Verse
from chapter import Chapt

#Messages for different error response
message = {400:"Bad Request: The request was unacceptable due to wrong parameter(s).",401:"Unauthorized: Invalid access_token used.",402:"Request Failed.",404:"Not Found: The chapter/verse number you are looking for could not be found.",500:"Server Error: Something went wrong on our end."}



#Authentication from access_token
def auth_token(token):
  os.environ["gita_access_token"] = token



#Authentication from client_id and client_secret
def auth(client_id,client_secret):
  try:
    request = post("https://bhagavadgita.io/auth/oauth/token",data={"client_id":client_id,"client_secret":client_secret,"grant_type":"client_credentials","scope":"verse chapter"})
  except:
    print("Unable to send post request")
    return
  token = request.json()["access_token"]
  os.environ["gita_access_token"] = token
  return "You are authenticated by the generated token "+token



#function to get chapter(s) to get a single chapter pass the chapter number, to get all chapter don't pass anything.To get chapter(s) in hindi pass language="hi" ,by default language is English
def get_chapter(chapter_number=None, language="en"):
  if chapter_number == None:
    return Chapter.all()
  else:
    token = os.environ.get("gita_access_token")
    if language == "hi":
      url = "https://bhagavadgita.io/api/v1/chapters/{chapter_number}?access_token={token}&language=hi".format(chapter_number=chapter_number,token=token)
    else:
      url = "https://bhagavadgita.io/api/v1/chapters/{chapter_number}?access_token={token}".format(chapter_number=chapter_number,token=token)
    try:
      request = get(url)
    except:
      print("unable to send get request")
      return 
    if request.status_code == 200:
      response = request.json()
    else:
      print(message[request.status_code])
      return
    return Chapter(response,language)
    
 
      
#function to get verse(s). To get a specific verse pass chapter number and verse number ,to get list of all verses from a specific chapter pass only chapter number, to get list of all verses from all chaters pass nothing.To get verse(s) in hindi pass language="hi" ,by default language is English
def get_verse(chapter_number=None,verse_number=None,language="en"):
  token = os.environ.get("gita_access_token")
  if token is None:
    print("Authentication not done")
    return
  if verse_number==None and chapter_number==None:
    return Verse.all(language=language)
  elif verse_number==None:
    return Verse.all(chapter_number,language=language)
  
  elif chapter_number == None:
    print("Please pass enough arguments")
  else:
    if language=="hi":
      url = "https://bhagavadgita.io/api/v1/chapters/{chapter_number}/verses/{verse_number}?access_token={token}&language={language}".format(chapter_number=chapter_number,verse_number=verse_number,language=language,token=token)
    else:
      url = "https://bhagavadgita.io/api/v1/chapters/{chapter_number}/verses/{verse_number}?access_token={token}".format(chapter_number=chapter_number,verse_number=verse_number,token=token)
    try:
      request = get(url)
    except:
      print("unable to send get request")
      return 
    if request.status_code == 200:
      response = request.json()
    else:
      print(message[request.status_code])
      return
    return Verse(json_data=response,language=language)
    
    
  
  
