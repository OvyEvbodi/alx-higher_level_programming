#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response
curl -sX PUT -L -d "You%20got%20me!" -H "Content-Type: text/html; charset=UTF-8" 0.0.0.0:5000/catch_me;
