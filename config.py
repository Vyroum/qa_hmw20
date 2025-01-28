import os


deviceName = os.getenv('deviceName')
appWaitActivity = os.getenv('appWaitActivity', 'org.wikipedia.*')
app = os.getenv('app', 'bs://8a09749887e68fdf72a7e75c2c30c119bf94e285')
is_bstack = app.startswith('bs://')
remote_url = os.getenv('remote_url', 'http://127.0.0.1:4723')
if is_bstack:
    remote_url = 'http://hub.browserstack.com/wd/hub'
