import os
import sys
from clear_screen import clear
from lib.colors import style
from lib.token import get_credentials
from lib.ids import dump_ids
from lib.phones import dump_phones
from lib.emails import dump_emails
from lib.user_info import dump_info


# Main function
def main_function():
    while True:
        if os.path.isdir('Logs') == False:
            os.mkdir('Logs')
        else:
            None
        if os.path.isdir('lib/cache') == False:
            os.mkdir('lib/cache')
        else:
            None
        clear()
        
        print('     --- Welcome to FB-ID_Dump ---')
        print('        --- Author: FALCON ---')

        # Menu options
        print(style.GREEN('\n[1]') + style.RESET(' Generate access token.'))
        print(style.BLUE('[2]') + style.RESET(" Dump all IDs."))
        print(style.WHITE('[3]') + style.RESET(" Dump all phone numbers."))
        print(style.GREEN('[4]') + style.RESET(' Dump all email addresses.'))
        print(style.BLUE('[5]') + style.RESET(' Full information search by ID/Username.'))
        print(style.RED('[6]') + style.RED(' Exit FB-ID_Dump.'))
        try:
            mode_option = int(input(style.YELLOW('\n[+]') + style.RESET(" Enter your option number: ")))
        except:
            print(style.RED('\n[!]') + style.RESET(' Error: User exited.'))
            sys.exit(0)

        if mode_option == 1:
            get_credentials()
        elif mode_option == 2:
            dump_ids()
        elif  mode_option == 3:
            dump_phones()
        elif mode_option == 4:
            dump_emails()
        elif mode_option == 5:
            dump_info()
        elif mode_option == 6:
            print(style.RED('[!]') + style.RESET(' User exit, exiting...'))
            sys.exit(0)


if __name__ == "__main__":
    clear()
    print('     ---$##  Welcome to FB-ID_Dump $## ---')
    print('        --- Author: FALCON --')
    print(style.GREEN('\n[+]') + style.RESET(' Notes:'))
    print(style.YELLOW('    [*]') + style.RESET(' I am not responsible for any damage caused by FB-ID_Dump!'))
    print(style.YELLOW('    [*]') + style.RESET(" Read the readme.md page carefully before using FB-ID_Dump!"))
    print(style.YELLOW('    [*]') + style.RESET(" Abusing this script might end with locking up your Facebook account until you verify it again!"))
    try:
        warning = str(input(style.RED('\n[!]') + style.RESET(' Do you agree to use FB-ID_Dump for educational purposes only (y/n): ')))
    except KeyboardInterrupt:
        print(style.RED('\n[!]') + style.RESET(' Error: User exited.'))
        sys.exit(0)
    main_function() if warning.lower() == "y" else sys.exit(0)
