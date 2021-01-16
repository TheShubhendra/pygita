"""Module of execption classes."""


class PygitaExceptions(Exception):
    """Base class for exceptions."""
    pass


class BadRequestError(PygitaExceptions):
    """Bad Request: The request was unacceptable
due to wrong parameter(s)."""
    pass


class UnauthorisedError(PygitaExceptions):
    """Unauthorized: Invalid access_token used."""
    pass


class RequestFailedError(PygitaExceptions):
    """API requested fail from server side."""
    pass


class NotFoundError(PygitaExceptions):
    """Not Found: The chapter/verse number you are
looking for could not be found."""
    pass


class ServerError(PygitaExceptions):
    """Server Error: Something went wrong on our end."""
    pass
