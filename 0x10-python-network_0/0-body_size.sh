#!/bin/bash
# This script sends a request to a url and displays the response size
curl -s "$1" | wc -c
