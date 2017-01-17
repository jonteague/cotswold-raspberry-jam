#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "USAGE: sdimage.sh <img-file-to-copy>"
    exit
fi

if [ ! -f $1 ]; then
    echo "File '{$1}' not found!"
    exit
fi

while [ 1 ]
do
    START_LIST=$(diskutil list | grep /dev/disk | awk '{print $1}')
    NOW_LIST=${START_LIST}

    echo "Found these drives"
    echo "${START_LIST}"
    echo ""
    echo "Insert an SD card"

    until [ $(comm -13 <(echo "${START_LIST}") <(echo "${NOW_LIST}") | wc -l ) -ne 0  ]; do
      sleep 1
      NOW_LIST=$(diskutil list | grep /dev/disk | awk '{print $1}')
    done

    NEW_DRIVE=$(comm -13 <(echo "${START_LIST}") <(echo "${NOW_LIST}"))

    echo "New drive: ${NEW_DRIVE}"

    if [ $(echo "${NEW_DRIVE}" | wc -l) -ne 1 ]; then
        echo "ERROR: Too many drives added!"
        exit
    fi

    sleep 1
    
    diskutil unmountDisk ${NEW_DRIVE}
    if [ $? -ne 0 ]; then
        echo "ERROR: Unable to unmount ${NEW_DRIVE}"
        exit
    fi

    NEW_RDRIVE=$(echo ${NEW_DRIVE} | sed 's|/dev/disk|/dev/rdisk|g')

    echo "Writing to: ${NEW_RDRIVE} - this will take some time"

    dd bs=1m if=${1} of=${NEW_RDRIVE}
    if [ $? -ne 0 ]; then
        echo "ERROR: Disk image copy failed"
        exit
    fi
    sync

    echo "Write complete, disks now:"
    echo "$(diskutil list | grep /dev/disk | awk '{print $1}')"

    diskutil eject ${NEW_DRIVE}
    if [ $? -ne 0 ]; then
        echo "ERROR: Unable to eject ${NEW_DRIVE}"
        exit
    fi
    
    sleep 1
    
    echo "Remove SD card and press any key to continue"
    read -rsn1
    
done

echo "Goodbye ..."
