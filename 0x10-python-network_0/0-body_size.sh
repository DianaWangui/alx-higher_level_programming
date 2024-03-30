#!/bin/bash
# This script sends a request to a URL and displays the size
curl -s "$1" | wc -c