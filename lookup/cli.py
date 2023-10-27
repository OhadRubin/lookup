import fire
from redis import StrictRedis
from socket import gethostname
from typing import Optional,Any
import os
import sys
import json


def lset(data:Any, hostname:Optional[str]=None):
    url = os.environ["REDIS_URL"]
    if hostname is None:
        hostname = gethostname()
    data = json.dumps(data)
    rdict = StrictRedis.from_url(url)
    rdict.set(hostname, data.encode())


def lget(hostname:Optional[str]=None):
    url = os.environ["REDIS_URL"]
    if hostname is None:
        hostname = gethostname()
    rdict = StrictRedis.from_url(url)
    out = json.loads(rdict.get(hostname).decode())
    return out 


def get_set_argv():
    if len(sys.argv)==1:
        sys.argv = lget(url)
    else:
        lset(url, sys.argv)

def main():
    fire.Fire()


if __name__ == '__main__':
    main()
