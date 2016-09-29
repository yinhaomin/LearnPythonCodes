import sys
import os
import os.path
import urlparse
import contextlib
import urllib
import httplib
import base64
import json
import urllib2
import socket
import time
import random

def prepare_request():
    """ prepare request for service
    Args:
        path: image path in disk
    Returns:
        req_json: json string of request data
    """

    logid = random.randint(1000000, 100000000)
    """data = prepare_data(path)
    """
    req_array = {
                    'appid': '123456',
                    'logid': logid,
                    'format': 'json',
                    'from': 'test-python',
                    'cmdid': '123',
                    'clientip': '0.0.0.0',
                    'data': 'china',
                }
    req_json = json.dumps(req_array)
    return req_json
if __name__ == '__main__':
    req_json = prepare_request()
    print "Succed to generate thumb for %s" % (req_json)
    
