import os

deviceName = os.getenv('DEVICE_NAME')
appWaitActivity = os.getenv('appWaitActivity', 'org.wikipedia.*')
is_bstack = os.getenv('USE_BSTACK', 'false').strip().lower() == 'true'

if is_bstack:
    app = os.getenv('APP_KEY')

else:
    app = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        os.getenv('app', 'app-alpha-universal-release.apk')
    ))

remote_url = (
    'https://hub.browserstack.com/wd/hub'
    if is_bstack
    else 'http://127.0.0.1:4723'
)
