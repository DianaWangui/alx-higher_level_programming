#!/bin/bash
# Send a GET request to the URL with the header variable X-School-User-Id set to 98
curl -sL -H "X-School-User-Id: 98" "$1"
