import os

from dotenv import load_dotenv

import utils.file_location as file_location

load_dotenv(override=True)

deviceName = os.getenv('DEVICE_NAME')
appWaitActivity = os.getenv('appWaitActivity', 'org.wikipedia.*')
is_bstack = os.getenv('USE_BSTACK', 'false').lower() == 'true'

if is_bstack:
    app = os.getenv('APP_KEY')
else:
    app_env = os.getenv('app', 'app-alpha-universal-release.apk')
    app = file_location.path_to_file(app_env)

remote_url = (
    'https://hub.browserstack.com/wd/hub'
    if is_bstack
    else os.getenv('remote_url', 'http://127.0.0.1:4723'))
