import json
from functools import wraps
from cape_api_helpers.exceptions import UserException
from cape_api_helpers.text_responses import ERROR_REQUIRED_PARAMETER, ERROR_INVALID_BOUNDING_BOX, ERROR_INVALID_JSON


def required_parameter(request, parameter):
    if parameter.lower() not in request['args']:
        raise UserException(ERROR_REQUIRED_PARAMETER % parameter)
    return request['args'][parameter.lower()]


def optional_parameter(request, parameter, default):
    if parameter.lower() in request['args']:
        return request['args'][parameter.lower()]
    else:
        return default


def list_document_ids(wrapped):
    """
    Decorator for handling API calls that take as input a list of document ids.
    Calls the wrapped function with the parsed document ids
    selected by the API user.
    """
    @wraps(wrapped)
    def decorated(request, *args, **kwargs):
        if 'documentids' in request['args']:
            if '[' == request['args']['documentids'][0]:
                document_ids = json.loads(request['args']['documentids'])
            else:
                document_ids = request['args']['documentids'].split(',')
        else:
            document_ids = None
        return wrapped(request,*args,**kwargs,document_ids=document_ids)

    return decorated


def list_saved_reply_ids(wrapped):
    """
    Decorator for handling API calls that take as input a list of saved reply ids.
    Calls the wrapped function with the parsed saved reply ids selected by the
    API user.
    """
    @wraps(wrapped)
    def decorated(request, *args, **kwargs):
        if 'savedreplyids' in request['args']:
            if '[' == request['args']['savedreplyids'][0]:
                saved_reply_ids = json.loads(request['args']['savedreplyids'])
            else:
                saved_reply_ids = request['args']['savedreplyids'].split(',')
        else:
            saved_reply_ids = None
        return wrapped(request, *args, **kwargs, saved_reply_ids=saved_reply_ids)

    return decorated


def list_annotation_ids(wrapped):
    """
    Decorator for handling API calls that take as input a list of annotation ids.
    Calls the wrapped function with the parsed annotation ids selected by the
    API user.
    """
    @wraps(wrapped)
    def decorated(request, *args, **kwargs):
        if 'annotationids' in request['args']:
            if '[' == request['args']['annotationids'][0]:
                annotation_ids = json.loads(request['args']['annotationids'])
            else:
                annotation_ids = request['args']['annotationids'].split(',')
        else:
            annotation_ids = None
        return wrapped(request, *args, **kwargs, annotation_ids=annotation_ids)

    return decorated


def list_bounding_boxes(wrapped):
    """
    Decorator for handling API calls that take as input a list of bounding boxes.
    Calls the wrapped function with the parsed bounding boxes provided by the
    API user.
    """
    @wraps(wrapped)
    def decorated(request, *args, **kwargs):
        if 'boundingboxes' in request['args']:
            if '[' == request['args']['boundingboxes'][0]:
                bounding_boxes = json.loads(request['args']['boundingboxes'])
                for bounding_box in bounding_boxes:
                    required_keys = ['x1', 'y1', 'x2', 'y2']
                    for key in required_keys:
                        if key not in bounding_box.keys():
                            raise UserException(ERROR_INVALID_BOUNDING_BOX % key)
            else:
                raise UserException(ERROR_INVALID_JSON)
        else:
            bounding_boxes = None
        return wrapped(request, *args, **kwargs, bounding_boxes=bounding_boxes)

    return decorated


def list_pages(wrapped):
    """
    Decorator for handling API calls that take as input a list of pages.
    Calls the wrapped function with the parsed pages provided by the
    API user.
    """
    @wraps(wrapped)
    def decorated(request, *args, **kwargs):
        if 'pages' in request['args']:
            if '[' == request['args']['pages'][0]:
                pages = json.loads(request['args']['pages'])
            else:
                pages = [int(page) for page in request['args']['pages'].split(',')]
        else:
            pages = None
        return wrapped(request, *args, **kwargs, pages=pages)

    return decorated


def dict_metadata(wrapped):
    """
    Decorator for handling API calls that provide a metadata dictionary as input.
    Calls the wrapped function with the parsed metadata provided by the API user.
    """
    @wraps(wrapped)
    def decorated(request, *args, **kwargs):
        if 'metadata' in request['args']:
            metadata = json.loads(request['args']['metadata'])
        else:
            metadata = None
        return wrapped(request, *args, **kwargs, metadata=metadata)

    return decorated
