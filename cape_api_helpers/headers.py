
def generate_cors_headers(request):
    CORS_HEADERS = {'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Credentials': 'true',
                    'Access-Control-Allow-Methods': 'GET, POST, PATCH, PUT, DELETE, OPTIONS',
                    'Access-Control-Allow-Headers': 'Origin, Content-Type, X-Auth-Token'}

    # To support full cross site access we need to add the requesting origin to the access control headers explicitly
    for header in request.headers.keys():
        if header.lower() == 'origin':
            CORS_HEADERS['Access-Control-Allow-Origin'] = request.headers['origin']
            break

    return CORS_HEADERS