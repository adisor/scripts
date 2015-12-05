#!/usr/bin/env python3

import sys
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

patches = [
        {"name": "XS65ESP1", "url": "server/XS65ESP1.xsupdate"},
        {"name": "XS65ESP1003", "url": "server/XS65ESP1003.xsupdate"},
        {"name": "XS65ESP1005", "url": "server/XS65ESP1005.xsupdate"},
        {"name": "XS65ESP1009", "url": "server/XS65ESP1009.xsupdate"},
        {"name": "XS65ESP1010", "url": "server/XS65ESP1010.xsupdate"},
        {"name": "XS65ESP1011", "url": "server/XS65ESP1011.xsupdate"},
        {"name": "XS65ESP1014", "url": "server/XS65ESP1014.xsupdate"},
]


def main(argv):
    # Select patch
    select = 0
    while True:
        print("Select which patch to apply:")
        count = 0
        while count < len(patches):
            exists = ''
            exists =  os.popen("xe patch-list name-label="+patches[count]['name']).read().rstrip()
            if exists != '':
                print(bcolors.OKGREEN + " " + str(count) + ": " + patches[count]['name'] + " " + bcolors.ENDC)
            else:
                print(bcolors.FAIL + " " + str(count) + ": " + patches[count]['name'] + " " + bcolors.ENDC)
            count = count + 1

        select = int(raw_input('Enter your input: '))

        if (select >= 0 and select < len(patches)):
            break

    # download patch
    os.system("wget " + patches[select]['url'])

    # unzip
    #os.system("unzip "+ patches[select]['name']+".zip")

    # Add to xe patch-upload
    os.system("xe patch-upload file-name="+patches[select]['name']+".xsupdate")

    # Get host uuid
    uuid = os.popen("xe host-list | awk '/uuid/ {print $5;}'").read().rstrip()

    # Get patch uuid
    puuid = os.popen("xe patch-list name-label="+patches[select]['name']+" | awk '/uuid/ {print $5;}'").read().rstrip()

    # Apply patch
    os.system("xe patch-apply host-uuid="+uuid+" uuid="+puuid)

    # remove patches
    os.system("rm -f "+patches[select]['name']+"*")

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
