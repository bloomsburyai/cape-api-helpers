# Copyright 2018 BLEMUNDSBURY AI LIMITED
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from logging import debug

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
    debug(f'Added CORS headers to request {getattr(request,"url",None)}')
    return CORS_HEADERS
