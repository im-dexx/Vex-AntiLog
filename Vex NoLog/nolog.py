#================================#
# █░█ █▀▀ ▀▄▀ ▄▄ █▀▄ █▀▀ █░█     #
# ▀▄▀ ██▄ █░█ ░░ █▄▀ ██▄ ▀▄▀     #

# https://github.com/im-dexx     #
#================================#

# Libraries =======|
import os

# Functions =======|


# Variables =======|


# NoLog ===========|
def scanner():
    file = input("File Path: ")

    try:
        scan = open(file, "r")
    except:
        print("error, please try again.")
        scanner()

    for line in scan:
        checkip1 = line.split("ip")

        checkwebhook1 = line.split("webhook")
        checkwebhook2 = line.split("discord")

        checklink1 = line.split("https")

        for x in checkip1:
            print("IP Logger found: looked for 'ip'")
        for x in checkwebhook1:
            print("Webhook found: looked for 'webhook'")
        for x in checkwebhook2:
            print("Webhook found: looked for 'discord'")
        for x in checklink1:
            print("Link found: looked for 'https'")

    print("\n")
    scanner()
scanner()
