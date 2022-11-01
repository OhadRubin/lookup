import os
from slack import WebClient
from appdirs import user_cache_dir

cache_path = user_cache_dir("alerts", "alerts")
import fire
import os
os.makedirs(cache_path, exist_ok=True)
import json
from loguru import logger

def get_token():
  assert os.path.exists(f"{cache_path}/credentials.json"), "Please login first"
  with open(f"{cache_path}/credentials.json") as f:
        return json.load(f)["token"]
  
def send_message(message,token=None,channel="ohad_alerts"):
  if token is None:
    token = get_token()  
  client = WebClient(token=token)
  
  client.chat_postMessage(
    channel=channel,
    text=message,
  )


def main_loop(cmd:str, message=None,token=None):
    if cmd == "msg":
        send_message(message,token)
    elif cmd == "login":
      with open(f"{cache_path}/credentials.json","w") as f:
        json.dump(dict(token=token),f)
      logger.info("Saved credentials")
    else:
        print("Unknown command")
    
def main():
    fire.Fire(main_loop)

if __name__ == '__main__':
    main()
