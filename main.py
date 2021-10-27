import subprocess
import requests

# Detect if connected to bridge
wifi_name = 'HUAWEI-4211-2.4G'

if wifi_name in subprocess.check_output('netsh wlan show interfaces').decode('utf-8'):
    # Connected
    r = requests.get('https://www.btwifi.com:8443')
    if 'logged on to BT Wi-Fi' in r.text:
        print('Logged in')
    else:
        print('Not logged in')