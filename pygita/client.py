""" API Client module for handling requests and responses. """
import requests
from .exceptions import (PygitaException,
                         ConnectionError,
                         BadRequestError,
                         UnauthorisedError,
                         RequestFailedError,
                         NotFoundError,
                         ServerError,
                         AuthorizationError,
                        )

class Client:
    """ API Client module for handling requests and responses. """

    def __init__(self,
                 CLIENT_ID,
                 CLIENT_SECRET,
                 grant_type = None,
                 scope = None,
                 ):
        """
            Client object constructer.
            parameters:
                -CLIENT_ID: Obtained from Account Dashboard after registering an app on https://bhagavadgita.io
                -CLIENT_SECRET: Obtained from Account Dashboard after registering an app on https://bhagavadgita.io.
                -grant_type: Grant type (optional).
                    Default value: client_credentials.
                -scope: The resources that you would like to access(optional).
                    Value: verse, chapter, verse chapter
                    Default value: verse chapter
            Returns the Client object.
        """
        if grant_type is None:
            grant_type = 'client_credentials'
        if scope is None:
            scope = 'verse chapter'
        self.CLIENT_ID = CLIENT_ID
        self.CLIENT_SECRET = CLIENT_SECRET
        self.grant_type = grant_type
        self.scope = scope
        self.__API__BASE_URL = 'https://bhagavadgita.io'
        self.__API__END_POINT = '/api/v1/'
        self.__API__TOKEN_END_POINT = '/auth/oauth/token'

    def __apiRequest(self, url, params):
        """
            Used internally by the Client object to make calls to the API.
            Parameters:
                -url: the URL of the API endpoint.
                -params: parameters for the request.
            Returns the JSON response in the form of a Dictionary.
            Otherwise, an exception is raised.
        """
        params["access_token"] = self.get_token()
        try:
            response = requests.get(url, params)
        except requests.exceptions.RequestException:
            raise ConnectionError('Failed to connect to bhagavadgita.io.')
        response_code = response.status_code
        if response_code == 400:
            raise BadRequestError("Wrong parameters are passed")
        elif response_code == 401:
            raise UnauthorisedError("Your access_token is not valid")
        elif response_code == 402:
            raise RequestFailedError("Request Failed")
        elif response_code == 500:
            raise ServerError("Server side error")
        else:
            try:
                response.raise_for_status()
                response = response.json()
            except ValueError:
                raise PygitaException("Server returned invalid response.")
            except:
                raise PygitaException("An unknown error occurred during the parsing of response.")
        return response

    def request_token(self):
        """
            Requests an access_token from the API.
            Returns token if access_token is successfully obtained.
            Otherwise, an exception is raised.
        """
        try:
            request = post('https://bhagavadgita.io/auth/oauth/token',
                           data={
                                 'client_id': self.CLIENT_ID,
                                 'client_secret': self.Client_secret,
                                 'grant_type': self.grant_type,
                                 'scope': self.scope,
                                  })
            token = request.json()['access_token']
        except:
            raise AuthorizationError("Unable to get access_token.")
        return token

    def __request_verse(self, chapter_number, verse_number, language):
        params = {"language":language}
        url = self.__API__BASE_URL+self.__API__END_POINT+f'/chapter/{chapter_number}/verse/{chapter_number}'
        self.__apiRequest(url, params)

    def get_verse(self, chapter_number, verse_number, language="en"):
        json_data = self.__request_verse(chapter_number, verse_number, language)
        return Verse(self, json_data)