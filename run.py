import gspread
from google.oauth2.service_account import credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

def sharkfin_logo():
    """
    Logo for the game. Generated with: https://patorjk.com/
    """
    print(Style.BLUE + """
        

  /$$$$$$  /$$                           /$$             /$$$$$$$$ /$$          
 /$$__  $$| $$                          | $$            | $$_____/|__/          
| $$  \__/| $$$$$$$   /$$$$$$   /$$$$$$ | $$   /$$      | $$       /$$ /$$$$$$$ 
|  $$$$$$ | $$__  $$ |____  $$ /$$__  $$| $$  /$$/      | $$$$$   | $$| $$__  $$
 \____  $$| $$  \ $$  /$$$$$$$| $$  \__/| $$$$$$/       | $$__/   | $$| $$  \ $$
 /$$  \ $$| $$  | $$ /$$__  $$| $$      | $$_  $$       | $$      | $$| $$  | $$
|  $$$$$$/| $$  | $$|  $$$$$$$| $$      | $$ \  $$      | $$      | $$| $$  | $$
 \______/ |__/  |__/ \_______/|__/      |__/  \__/      |__/      |__/|__/  |__/
                                                                                
                                                                                
                                                                                


    """ + Style.RESET)