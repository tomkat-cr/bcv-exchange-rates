import sys
import json

from fastapi import FastAPI
from a2wsgi import ASGIMiddleware

from bcv_exchange_rates.bcv import get_bcv_exchange_rates


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
    print(json.dumps(get_bcv_exchange_rates()))


api = FastAPI()
app = ASGIMiddleware(api)


@api.get("/get_bcv_exchange_rates")
def get_bcv_rates():
    api_response = get_bcv_exchange_rates()
    # return json.dumps(api_response)
    return api_response
