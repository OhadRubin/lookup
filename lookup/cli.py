import fire
from redis import StrictRedis
from socket import gethostname

def set(url:str, data:str):
    hostname = gethostname()
    rdict = StrictRedis.from_url(url)
    rdict.set(hostname, data.encode())


def get(url:str):
    hostname = gethostname()
    rdict = StrictRedis.from_url(url)
    return rdict.get(hostname).decode()
    

if __name__ == '__main__':
    fire.Fire()
