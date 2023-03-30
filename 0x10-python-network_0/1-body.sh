#!/bin/bash
# Takes in a URL, sends a GET request to the URL, and displays the body of the response
status_code=$(curl -H "Connection: Keep-Alive" -s -D- "$1" | grep "HTTP" | cut -d " " -f2); if [ "$status_code" -eq 200 ]; then  curl -s "$1"; fi
