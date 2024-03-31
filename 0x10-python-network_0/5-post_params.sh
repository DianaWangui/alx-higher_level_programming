#!/bin/bash
# Send a GET request to the URL with the header variable X-School-User-Id set to 98
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
