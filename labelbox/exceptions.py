class LabelboxError(Exception):
    """Base class for exceptions."""
    def __init__(self, message):
        self.message = message


class AuthenticationError(LabelboxError):
    """Raised when an API key fails authentication."""
    pass


class AuthorizationError(LabelboxError):
    """Raised when a user is unauthorized to perform the given request."""
    pass


class MalformedRequestError(LabelboxError):
    """Raised when an invalid request is made."""
    pass


class ResourceNotFoundError(LabelboxError):
    """Exception raised when a given resource is not found. """

    def __init__(self, db_object_type, params):
        """ Constructor.
        Args:
            db_object_type (type): A labelbox.schema.DbObject subtype.
            params (dict): Dict of params identifying the sought resource.
        """
        super().__init__("Resouce '%s' not found for params: %r" % (
            db_object_type.type_name(), params))
        self.db_object_type = db_object_type
        self.params = params


class ValidationFailedError(LabelboxError):
    """Exception raised for when a GraphQL query fails validation (query cost, etc.)

       E.g. a query that is too expensive, or depth is too deep.
    """
    pass


class InvalidQueryError(LabelboxError):
    """ Indicates a malconstructed or unsupported query (either by GraphQL in
    general or by Labelbox specifically). This can be the result of either client
    or server side query validation. """
    pass


class NetworkError(LabelboxError):
    """Raised when an HTTPError occurs."""
    def __init__(self, cause, message=None):
        if message is None:
            message = str(cause)
        super().__init__(message)
        self.cause = cause
