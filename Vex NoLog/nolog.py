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
def nolog():
    # ask4input
    print("Drag & Drop the file (Remove the '' at the start and end)")
    file2check = input("File to check?> ")

    # scan file
    try:
        scan = open(file2check, "r")
    except:
        print("Invalid File, try again.")
        nolog()

    for line in scan:
        check4webhook1 = line.split("discord")
        check4webhook2 = line.split("webhooks")
        check4webhook3 = line.split("api")
        
        check4link1 = line.split("https")
        check4link2 = line.split("://")
        check4link3 = line.split("com")

        check4ip1 = line.split("ip")

        for x in check4webhook1:
            print("Webhook found: scanned for 'discord'")
        for x in check4webhook2:
            print("Webhook found: scanned for 'webhooks'")
        for x in check4webhook3:
            print("Webhook found: scanned for 'api'")

        for x in check4link1:
            print("Link Found: scanned for 'https'")
        for x in check4link2:
            print("Link Found: scanned for '://'")
        for x in check4link3:
            print("Link Found: scanned for 'com'")

        for x in check4ip1:
            print("IP Logger Found: scanned for 'ip'")

    # loop
    nolog()
nolog()