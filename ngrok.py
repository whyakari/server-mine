import os
from dotenv import load_dotenv
from pyngrok import ngrok, conf, exception
import time
import threading

load_dotenv()

token = os.getenv('TOKEN_NGROK', '')

def connect(token, port, region):
    account = None
    if token == None:
        token = 'None'
    else:
        if ':' in token:
            account = token.split(':')[1] + ':' + token.split(':')[-1]
            token = token.split(':')[0]

    config = conf.PyngrokConfig(
        auth_token=token, region=region
    )
    try:
        if account == None:
            public_url = ngrok.connect(port, proto="tcp", pyngrok_config=config).public_url
        else:
            public_url = ngrok.connect(port, proto="tcp", pyngrok_config=config, auth=account).public_url
    except exception.PyngrokNgrokError:
        print(f'Invalid ngrok authtoken, ngrok connection aborted.\n'
              f'Your token: {token}, get the right one on https://dashboard.ngrok.com/get-started/your-authtoken')
        return None

    return public_url

def keep_ngrok_running(token, port, region, duration_minutes):
    public_url = connect(token, port, region)
    if public_url is not None:
        print(f'ngrok connected! URL: {public_url}\n'
              f'ngrok will remain running for {duration_minutes} minutes.')
        time.sleep(duration_minutes * 60)
        ngrok.disconnect(public_url)
        print('ngrok disconnected.')

if __name__ == "__main__":
    duration_minutes = 10
    threading.Thread(target=keep_ngrok_running, args=(token, 25565, 'us', duration_minutes)).start()

