#!/bin/bash
#  send put request to 0.0.0.0:5000/catch_me and get the res body
curl -sLX PUT -d "user_id=You got me!" 0.0.0.0:5000/catch_me
