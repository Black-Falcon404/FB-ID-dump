import sys
import json
import getpass
import hashlib
import requests
from clear_screen import clear
from lib.colors import style


def generate_token(data):
    while True:
        print(style.YELLOW('\n[*]') + style.RESET(' Generating access token...'))
        try:
            req = requests.get('https://api.facebook.com/restserver.php',params=data)
            json_token = json.loads(req.text)
            with open('lib/cache/facebook_token.txt', 'w') as json_file:
                json_file.write(json_token['access_token'])
            print(style.GREEN('[+]') + style.RESET(' Saved token successfuly in lib/cache/facebook_token.txt'))
        except KeyError:
            print(style.RED('\n[!]') + style.RESET(' Error: Login failed, make sure the credentials you used are right and 2FA is turned off.'))
            sys.exit(0)
        except KeyboardInterrupt:
            print(style.RED('\n[!]') + style.RESET(' Error: User exited.'))
            sys.exit(0)
        except requests.ConnectionError:
            print(style.RED('\n[!]') + style.RESET(' Error: Failed to generate access token due to connection error.'))
            sys.exit(0)
        input(style.CYAN('[*]') + style.RESET(' Press any key to go back to the main menu.'))
        break


# Get user facebook credentials and generate api link parameters.
def get_credentials():
    clear()
    print('     --- Generate Facebook Access Token ---')
    print('           --- Author: Falcon ---\n')
    try:
        username = str(input(style.GREEN('[+]') + style.RESET(' Facebook email: ')))
    except KeyboardInterrupt:
        print(style.RED('\n[!]') + style.RESET(' Error: User exited.'))
        sys.exit(0)
    try:
        password = str(getpass.getpass(style.GREEN('[+]') + style.RESET(' Facebook password: ')))
    except KeyboardInterrupt:
        print(style.RED('\n[!]') + style.RESET(' Error: User exited.'))
        sys.exit(0)
    API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
    API_KEY = '882a8490361da98702bf97a021ddc14d'
    data = {
            "api_key":API_KEY,
            "credentials_type":"password",
            "email":username,
            "format":"JSON",
             "generate_machine_id":"1",
             "generate_session_cookies":"1",
             "locale":"en_US",
             "method":"auth.login",
             "password":password,
             "return_ssl_resources":"0",
             "v":"1.0"
             }
    sig = 'api_key=' + API_KEY + 'credentials_type=passwordemail='+username+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+password+'return_ssl_resources=0v=1.0'+API_SECRET

    hash = hashlib.new('md5')
    hash.update(sig.encode('utf-8'))
    data.update({'sig': hash.hexdigest()})
    generate_token(data)
