#!/bin/bash
# Takes in a URL, sends a GET req, displays the size of the body of the response
curl --head "$1" | grep "Content-Length" | cut -d " " -f2;
