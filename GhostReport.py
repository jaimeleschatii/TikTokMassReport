import threading
import requests
from colorama import Fore, Back, Style
import ctypes

count = 0

class GhostMain():
    banner = f"""
{Fore.RED}       _    {Fore.LIGHTRED_EX}            _   
{Fore.RED}      | |   {Fore.LIGHTRED_EX}           | |  
{Fore.RED}  __ _| |__ {Fore.LIGHTRED_EX}   ___  ___| |_ 
{Fore.RED} / _` | '_ \{Fore.LIGHTRED_EX}  / _ \/ __| __|
{Fore.RED}| (_| | | | |{Fore.LIGHTRED_EX}| (_) \__ \ |_ 
{Fore.RED} \__, |_| |_|{Fore.LIGHTRED_EX} \___/|___/\__|     
{Fore.RED}  __/ |                                       
{Fore.RED} |___/                       {Fore.RED}github.com/{Fore.LIGHTRED_EX}jaimeleschatii"""   
print(str(GhostMain.banner))

link = input(f"{Fore.RED}link {Fore.LIGHTRED_EX}{Fore.RED}[{Fore.LIGHTRED_EX}>{Fore.RED}] ")
username = input(f"{Fore.RED}username {Fore.LIGHTRED_EX}{Fore.RED}[{Fore.LIGHTRED_EX}>{Fore.RED}] ")
thrd =  input(f"{Fore.RED}Threads {Fore.RED}[{Fore.LIGHTRED_EX}>{Fore.RED}] ")

class Ghost:
    def main():
        while True:
            global count
            ctypes.windll.kernel32.SetConsoleTitleW("report " + str(count))
            headers = {
                'authority': 'www.tiktok.com',
                'sec-fetch-dest': 'empty',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'referer': f'https://www.tiktok.com/@{username}',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
                }
            GhostPost = requests.post(link, headers=headers)
            if GhostPost.status_code == 200:
                count += 1        
                print(f"{Fore.RED}[{Fore.LIGHTRED_EX}+{Fore.RED}] {Fore.LIGHTRED_EX}Succes report "+username)

    threads = []
    for threads in range(int(thrd)):
        t = threading.Thread(target=main)
        t.start()