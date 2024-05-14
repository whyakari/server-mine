import os
from dotenv import load_dotenv
from pyngrok import ngrok, conf, exception

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
        auth_token=token,
        region=region,
        ngrok_path="/usr/local/bin/ngrok"
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

