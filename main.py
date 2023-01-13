import requests
import os
import subprocess
from multiprocessing import Pool
from colorama import Fore, init
import time
from tqdm import tqdm
import random


init()





#ALL VANITY, REMOVE IF YOU WANT
def vanity():
    banner = """

     ▄████▄   ██░ ██ ▓█████   ██████   ██████     ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  
    ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██    ▒ ▒██    ▒    ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
    ▒▓█    ▄ ▒██▀▀██░▒███   ░ ▓██▄   ░ ▓██▄      ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
    ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄   ▒   ██▒  ▒   ██▒   ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
    ▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒██████▒▒▒██████▒▒   ▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
    ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░   ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
        ░  ▒    ▒ ░▒░ ░ ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░     ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
    ░         ░  ░░ ░   ░   ░  ░  ░  ░  ░  ░     ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ 
    ░ ░       ░  ░  ░   ░  ░      ░        ░     ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░     


    """

    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.LIGHTGREEN_EX + banner.replace("░", Fore.RED + "░" + Fore.LIGHTGREEN_EX).replace("▒", Fore.RED + "▒" + Fore.LIGHTGREEN_EX) + Fore.RESET)


    for i in tqdm(range(420)):
        time.sleep(random.uniform(0, 0.01))
        pass

    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.LIGHTGREEN_EX + banner.replace("░", Fore.RED + "░" + Fore.LIGHTGREEN_EX).replace("▒", Fore.RED + "▒" + Fore.LIGHTGREEN_EX) + Fore.RESET)
    time.sleep(0.3)

###################################################################################################################






def user_input():
    while True:
        choice = input("   [-] Which website would you like to check?\n   [1] Chess.com\n   [2] Lichess.org\n   ")
        if choice not in ('1', '2'):
            print(f"{Fore.RED}   [X] Invalid input. Please try again.{Fore.RESET}\n")
        else:
            print("\n")
            break
    while True:
        try:
            with open(input("   [-] Enter the name of the text file containing the usernames: ")) as f:
                usernames = f.read().splitlines()
                print("\n")
            break
        except FileNotFoundError:
            print(f"{Fore.RED}   [X] File not found. Please try again.\n{Fore.RESET}")
    while True:
        try:
            threads = int(input("   [-] Enter the number of threads you want to run: "))
            if threads <= 0:
                raise ValueError
            print("\n")
            break
        except ValueError:
            print(f"{Fore.RED}   [X] Invalid input. Please enter a whole number above 0.\n{Fore.RESET}")
    return choice, usernames, threads

def text_convert(file):
    with open(file) as f:
        usernames = f.read().splitlines()
    return usernames

def checker(choice, usernames, threads):
    checked = 0
    successes = 0
    failures = 0
    if choice == '1':
        site = "Chess.com"
        base_url = "https://www.chess.com/members/"
    else:
        site = "Lichess.org"
        base_url = "https://www.lichess.org/@/"
    while True:
        with Pool(threads) as p:
            results = p.map(check_username, [(base_url, username, site) for username in usernames])
        rate_limited = False
        for result, username in zip(results, usernames):
            if result is None:
                rate_limited = True
                break
            checked += 1
            if result:
                successes += 1
            else:
                with open("available.txt", "a") as f:
                    f.write(username + "\n")
                failures += 1
            subprocess.run(['title', f'ChessHunter | Checked: {checked} | Successes: {successes} | Failures: {failures} | Threads: {threads}'], shell=True)
        if not rate_limited:
            break
        time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n\n   Checked: {checked}\n   {Fore.GREEN}Successes: {successes}\n{Fore.RESET}   {Fore.RED}Failures: {failures}\n\n{Fore.RESET}")


def check_username(url_username_site):
    url, username, site = url_username_site
    response = requests.get(url + username)
    if response.status_code == 200:
        print(f'{Fore.RED}   [X] {username} is not available on {site}.{Fore.RESET}')
        return True
    elif response.status_code == 429:
        print(f'{Fore.YELLOW}   [!] Rate limit reached. Please try again later.{Fore.RESET}')
        time.sleep(3)
        return None
    else:
        print(f'{Fore.GREEN}   [+] {username} is available on {site}. {Fore.RESET}')
        return False



def main():
    vanity()
    choice, usernames, threads = user_input()
    checker(choice, usernames, threads)
    input("   [-] Press Enter to close.")




if __name__ == '__main__':
    vanity()
    choice, usernames, threads = user_input()
    checker(choice, usernames, threads)
    input("   [-] Press Enter to close.")
