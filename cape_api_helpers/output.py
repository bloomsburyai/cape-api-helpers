from functools import wraps

from cape_api_helpers.api_helpers_settings import SECRET_DEBUG_KEYWORD
from cape_api_helpers.exceptions import UserException
from cape_api_helpers.text_responses import ERROR_NUMERIC_REQUIRED, ERROR_TRUE_FALSE_BOTH_REQUIRED, \
    DEBUG_SERVER_CONNECTION_FAILURE


def list_response(wrapped):
    """
    Decorator for handling API calls that return a list of items.
    Calls the wrapped function with the number of items and offset
    requested by the API user.
    """

    @wraps(wrapped)
    def decorated(request, *args, **kwargs):
        number_of_items = None
        offset = None
        if 'numberofitems' in request['args']:
            if request['args']['numberofitems'].isnumeric():
                number_of_items = int(request['args']['numberofitems'])
            else:
                raise UserException(ERROR_NUMERIC_REQUIRED % 'numberOfItems')
        if 'offset' in request['args']:
            if request['args']['offset'].isnumeric():
                offset = int(request['args']['offset'])
            else:
                raise UserException(ERROR_NUMERIC_REQUIRED % 'offset')

        if number_of_items is not None and offset is not None:
            return wrapped(request, number_of_items, offset)
        elif number_of_items is not None:
            return wrapped(request, number_of_items)
        elif offset is not None:
            return wrapped(request, offset=offset)
        else:
            return wrapped(request)

    return decorated


def true_false_both_filter(request, items, parameter):
    """
    Filter a list of items based on an attribute being true, false or either.

    :param request: HTTP request
    :param items: list of items consisting of dictionaries
    :param parameter: The request argument to retrieve the filtering option from
    :return: A filtered list of items
    """
    if parameter in request['args']:
        test = request['args'][parameter].lower()
        if test == 'true':
            items = [item for item in items if item[parameter]]
        elif test == 'false':
            items = [item for item in items if not item[parameter]]
        elif test == 'both':
            # Otherwise return both true and false values
            pass
        else:
            raise UserException(ERROR_TRUE_FALSE_BOTH_REQUIRED % parameter)

    return items


def debuggable(wrapped):
    @wraps(wrapped)
    def decorated(request, *args, **kwargs):
        debug_server = request['args'].get(SECRET_DEBUG_KEYWORD, False)
        if debug_server:
            import pydevd
            import socket
            hostname, port = debug_server.split(":")
            port = int(port)
            try:
                # we cannot check if port is open since otherwise
                # setting the wrong hostname:port will trigger an irrecoverable system exit, because :
                # We cannot monkey patch due to pydevd already heavily monkey patching
                #      from _pydevd_bundle import pydevd_comm
                #      pydevd_comm.start_client = start_client...
                # And this makes weird and undefined behaviour:
                # s = socket.socket()
                # s.settimeout(0.5)
                # s.connect((hostname, port))
                # s.close()
                pydevd.settrace(host=hostname, stdoutToServer=True, stderrToServer=True, port=int(port))
            except Exception:
                raise UserException(DEBUG_SERVER_CONNECTION_FAILURE)
        try:
            result = wrapped(request, *args, **kwargs)
        finally:
            if debug_server:
                pydevd.stoptrace()
        return result

    return decorated
