import json
import sys

from fastapi import FastAPI
from a2wsgi import ASGIMiddleware

from get_bcv_exchange_rates import get_bcv_exchange_rates


def get_command_line_args():
    params = dict()
    params['mode'] = 'api'
    params['config_filename'] = '.env'
    if len(sys.argv) > 1:
        params['mode'] = sys.argv[1]
    if len(sys.argv) > 2:
        params['config_filename'] = sys.argv[2]
    return params


params = get_command_line_args()
if params['mode'] == 'cli':
    apiResponse = get_bcv_exchange_rates()
    print(apiResponse)

api = FastAPI()
app = ASGIMiddleware(api)


@api.get("/get_exchange_rates")
def get_rates():
    api_response = get_bcv_exchange_rates()
    # return json.dumps(api_response)
    return api_response
