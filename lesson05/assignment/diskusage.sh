#!/bin/bash

# Get the current date in the format ddmmyyyy
date=$(date +'%d%m%Y')

# Define the file name with the current date
filename="disk_usage_$date.txt"

echo "Disk#  %Usage  Current Free Space  Mount Point" > "$filename"
echo "---------------------------------------------" >> "$filename"

disks=$(df -h | awk '{print $1}' | grep "^/dev/")  # Get the list of disks

i=1
for disk in $disks; do
    usage=$(df -h | awk -v disk="$disk" '$1 == disk {print $5}')  # Get percentage usage
    free_space=$(df -h | awk -v disk="$disk" '$1 == disk {print $4}')  # Get current free space
    mount_point=$(df -h | awk -v disk="$disk" '$1 == disk {print $6}')  # Get mount point

    # Remove "i" from "gi" or "mi"
    usage=${usage//i/}
    free_space=${free_space//i/}

    printf "%-7s%-9s%-19s%s\n" "Disk$i" "$usage" "$free_space" "$mount_point" >> "$filename"
    ((i++))
done

echo "$filename"