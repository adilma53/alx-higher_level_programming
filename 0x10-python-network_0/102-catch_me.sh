#!/bin/bash
# send put request to 0.0.0.0:5000/catch_me and get the res body
curl -X POST -H "Content-Type: application/json" -d '{"catch_me": true}' http://0.0.0.0:5000/catch_me
