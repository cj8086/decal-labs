#!/bin/bash

# Check if a hostname argument has been provided
if [ -z "$1" ]; then
  echo "Usage: $0 <hostname>"
  exit 1
fi

# Ping the host once and check the exit status
ping -c 1 "$1" > /dev/null 2>&1

# Evaluate the exit status of the ping command
if [ $? -eq 0 ]; then
  echo "OK"
else
  echo "Host is not reachable"
fi