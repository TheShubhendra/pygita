"""Module of execption classes."""


class PygitaException(Exception):
    """Base class for exceptions."""
    pass

class ConnectionError(PygitaException):
    """Unable to connect with server."""
    pass


class BadRequestError(PygitaException):
    """Bad Request: The request was unacceptable
due to wrong parameter(s)."""
    pass


class UnauthorisedError(PygitaException):
    """Unauthorized: Invalid access_token used."""
    pass


class RequestFailedError(PygitaException):
    """API request failed from server side."""
    pass


class NotFoundError(PygitaException):
    """Not Found: The chapter/verse number you are
looking for could not be found."""
    pass


class ServerError(PygitaException):
    """Server Error: Something went wrong on server end."""
    pass


class AuthorizationError(PygitaException):
    """Unable to authorise using App credentials, Please cross check your CLIENT_ID and CLIENT_SECRET."""
    pass