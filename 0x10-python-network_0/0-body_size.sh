#!/bin/bash
# Takes in a URL, sends a GET req, displays the size of the body of the response
curl --head -s "$1" | grep "Content-Length" | cut -d " " -f2;
