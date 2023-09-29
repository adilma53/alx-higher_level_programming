#!/bin/bash
# display the length of reponse body of get request
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'