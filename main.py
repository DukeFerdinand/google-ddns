import os

import sentry_sdk
from requests import get

hostname = os.environ['TARGET_HOSTNAME']
sentry_sdk.init(
    os.environ['SENTRY_URI'],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    environment=f"kubernetes-job-for-{hostname}"
)

if __name__ == '__main__':
    print('Running google ddns job!')
    ip = get('https://api.ipify.org').text

    user = os.environ['GOOGLE_USER']
    password = os.environ['GOOGLE_PASS']

    if os.environ.get('DEBUG') is not None:
        print('DEBUG LOG')
        print('=========================')
        print('USER:', user)
        print('PASSWORD:', password)
        print('HOST:', hostname)
        print('=========================')

    print(f"Configuring: {hostname}")
    url = f'https://{user}:{password}@domains.google.com/nic/update?hostname={hostname}&myip={ip}'
    print("Updating public IP...")

    res = get(url)
    print('Request done, result:')
    print(res.text)
    print('Done! Check logs for statuses')
