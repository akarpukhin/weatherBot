import json
import os


def load_token(file_path='token.json'):
    with open(file_path, 'r') as file:
        token = json.load(file)
    return token.get('telegram_token'), token.get('weather_token')


def get_hostname():
    hostname = os.uname()[1]
    return hostname


HOSTNAME = get_hostname()

TELEGRAM_BOT_KEY, WEATHER_TOKEN = load_token()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_FILE = os.path.join(BASE_DIR, "logs/logs.log")

REQUEST_KWARGS = {
    'proxy_url': 'socks5://51.77.213.30:58222',
                 'urllib3_proxy_kwargs': {
                          'username': 'pruser',
                          'password': 'pruser'
                 }
}
