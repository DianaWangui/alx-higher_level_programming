#!/bin/bash
# Make a request to 0.0.0.0:5000/catch_me and display the body of the response
curl -sLX PUT 0.0.0.0:5000/catch_me -H "Origin: School"  -d "user_id=98"
